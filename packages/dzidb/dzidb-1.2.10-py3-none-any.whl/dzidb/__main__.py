import argparse
import json
import os
from collections import namedtuple

import wda
import tidevice


def cmd_devices(args):
    obj = tidevice.Device()
    ds = obj.usbmux.device_list()

    headers = ['UDID', 'SerialNumber', 'NAME', 'ProductVersion', "ConnType"]
    keys = ["udid", "serial", "name", "product_version", "conn_type"]
    tabdata = []
    for dinfo in ds:
        udid, conn_type = dinfo.udid, dinfo.conn_type
        _d = tidevice.Device(udid, obj.usbmux)
        name = _d.name
        serial = _d.get_value("SerialNumber")
        tabdata.append([udid, serial, name, _d.product_version, conn_type])
    result = []
    for item in tabdata:
        if args.l:
            result.append({key: item[idx] for idx, key in enumerate(keys)})
        else:
            result.append({"udid": item[0], "name": item[2]})
    print("List of devices attached")

    for device in result:
        if args.l:
            print(f"{device['udid']}\tdevice product:{device['name']} model:{device['name']} device:{device['name']}")
        else:
            print(f"{device['udid']}\tdevice")
    #json_result = json.dumps(result)
    #print(json_result)


def cmd_screencap(args):
    c = wda.USBClient(args.udid)
    # 规范化路径，确保使用/作为分隔符
    normalized_NamePath = os.path.normpath(args.fileName)
    normalized_PcPath = os.path.normpath(args.filePath)
    # 使用os.path.basename()获取文件名
    file_name = os.path.basename(normalized_NamePath)
    file_path = os.path.dirname(normalized_PcPath)
    fileName = os.path.join(file_path, file_name)
    c.screenshot().save(args.filePath, 'PNG')


def cmd_input_tap(args):
    c = wda.USBClient(args.udid)

    # 这里x，y必须得是int
    c.click(args.x, args.y, args.duration)


def cmd_input_swipe(args):
    c = wda.USBClient(args.udid)
    c.swipe(args.x1, args.y1, args.x2, args.y2, args.duration)


def cmd_input_text(args):
    c = wda.USBClient(args.udid)
    c.send_keys(args.text)


def cmd_home(args):
    c = wda.USBClient(args.udid)
    c.home()


def cmd_wm_size(args):
    c = wda.USBClient(args.udid)
    Size_Tuple = namedtuple('Size', ['width', 'height'])

    # 获取的size不对，均为实际的1/2
    # print(Size_Tuple(*(x * 2 for x in c.window_size())))
    print(f"Physical size: {c.window_size()[0] * 2}x{c.window_size()[1] * 2}")

def cmd_input_keyevent(args):
    c = wda.USBClient(args.udid)
    c.press_duration(args.keycode, args.duration)

def cmd_pull(args):
    print("OK")

def cmd_delete(args):
    print("OK")
commands = [
    dict(action=cmd_devices,
         command="devices",
         flags=[
             dict(args=['-l'],
                  action='store_true',
                  help='output one entry per line')
         ],
         help="show connected iOS devices"),
    dict(action=cmd_pull,
         command="screencap",
         flags=[
             dict(args=['-p'],
                  action='store_true',
                  help='output the screenshot in png format'),
             dict(args=['filename'],
                  metavar='FILENAME',
                  help='local output file path')
         ],
         help="capture the screen of an iOS device"),
    dict(action=cmd_delete,
         command="rm",
         flags=[
             dict(args=['useless'],
                  type=str,
                  help='useless')
         ]),
    dict(action=cmd_screencap,
         command="pull",
         flags=[
             dict(args=['fileName'],
                  type=str,
                  help='useless'),
             dict(args=['filePath'],
                  metavar='FILENAME',
                  help='local output file path')
         ],
         help="useless"),
    dict(action=None,  # 顶级命令不需要动作函数
         command="input",
         subcommands=[
             dict(action=cmd_input_tap,
                  command="tap",
                  flags=[
                      dict(args=['x'],
                           type=int,
                           help='x coordinate'),
                      dict(args=['y'],
                           type=int,
                           help='y coordinate'),
                      dict(args=['duration'],
                           type=float,
                           nargs='?',
                           help='tap hold duration')
                  ],
                  help="simulate a tap event at the specified coordinates"),
             dict(action=cmd_input_swipe,
                  command="swipe",
                  flags=[
                      dict(args=['x1'],
                           type=int,
                           help='x1 coordinate'),
                      dict(args=['y1'],
                           type=int,
                           help='y1 coordinate'),
                      dict(args=['x2'],
                           type=int,
                           help='x2 coordinate'),
                      dict(args=['y2'],
                           type=int,
                           help='y2 coordinate'),
                      dict(args=['duration'],
                           type=float,
                           nargs='?',
                           help='tap hold duration')
                  ],
                  help="simulate a swipe event at the specified coordinates"),
             dict(action=cmd_input_text,
                  command="text",
                  flags=[
                      dict(args=['text'],
                           type=str,
                           help='what to input'),
                  ],
                  help="simulate a input text event"),
             dict(action=cmd_input_keyevent,
                  command="keyevent",
                  flags=[
                      dict(args=['keycode'],
                           type=str,
                           help='code of physical button,one of <home|volumeUp|volumeDown|power|snapshot>'),
                      dict(args=['duration'],
                           type=float,
                           help='tap hold duration')
                  ],
                  help="simulate a tap event at the specified coordinates"),
         ],
         help="simulate input events"),
    dict(action=cmd_home,
         command="home",
         help="Back to the main screen"),
    dict(action=None,
         command="wm",
         subcommands=[
             dict(action=cmd_wm_size,
                  command="size",
                  help="gets the current device screen size"),
         ],
         help="windows manager commands")
]


def main():
    # 创建顶级解析器
    parser = argparse.ArgumentParser(
        description='Custom adb-like tool.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    # 设置共享参数
    parser.add_argument("-v", "--version", action="store_true", help="show current version"),
    parser.add_argument("-u", "--udid", help="specify unique device identifier")

    # 创建子解析器
    subparsers = parser.add_subparsers(dest='command')

    # 存储动作函数的字典
    actions = {}

    # 遍历命令列表
    for c in commands:
        cmd_name = c['command']
        cmd_aliases = c.get('aliases', [])
        cmd_help = c.get('help')
        cmd_flags = c.get('flags', [])
        cmd_action = c.get('action')
        cmd_subcommands = c.get('subcommands', [])

        # 为每个命令添加解析器
        sp = subparsers.add_parser(cmd_name, aliases=cmd_aliases, help=cmd_help,
                                   formatter_class=argparse.ArgumentDefaultsHelpFormatter)

        # 设置动作函数
        if cmd_action:
            sp.set_defaults(func=cmd_action)

        # 添加命令的标志
        for f in cmd_flags:
            args = f.get('args')
            kwargs = {k: v for k, v in f.items() if k != 'args'}
            sp.add_argument(*args, **kwargs)

        # 如果命令有子命令，则添加子解析器
        if cmd_subcommands:
            sub_subparsers = sp.add_subparsers(dest='subcommand')
            for sub_c in cmd_subcommands:
                sub_cmd_name = sub_c['command']
                sub_cmd_help = sub_c.get('help')
                sub_cmd_flags = sub_c.get('flags', [])
                sub_cmd_action = sub_c.get('action')

                # 为每个子命令添加解析器
                sub_sp = sub_subparsers.add_parser(sub_cmd_name, help=sub_cmd_help)

                # 设置子命令的动作函数
                sub_sp.set_defaults(func=sub_cmd_action)

                # 添加子命令的标志
                for f in sub_cmd_flags:
                    args = f.get('args')
                    kwargs = {k: v for k, v in f.items() if k != 'args'}
                    sub_sp.add_argument(*args, **kwargs)

    # 解析命令行参数
    args = parser.parse_args()

    # 调用相应的函数
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
