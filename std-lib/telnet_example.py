#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
不建议直接在 pycharm 运行
建议用 cmd 窗口执行该函数
"""

import telnetlib
import time


def do_telnet(host, username, password, commands):
    try:
        tn = telnetlib.Telnet(host, port=23, timeout=10)
    except:
        print('{host} 网络连接失败'.format(host=host))
        return False

    # 输入登录用户名
    tn.read_until('Username:')
    tn.write(username + '\n')

    # 输入登录密码
    tn.read_until('Password:')
    tn.write(password + '\n')

    time.sleep(2)
    command_result = tn.read_very_eager()
    if 'Local authentication is rejected' in command_result:
        print('{host} 登录失败，用户名或密码错误'.format(host=host))
        return False

    # 登录完毕后执行命令
    for command in commands:
        tn.write(command + '\n')
        time.sleep(2)
        command_result = tn.read_very_eager()
        print(command_result)

    # 执行完毕后，终止 Telnet 连接（或输入exit退出）
    tn.close()


if __name__ == "__main__":
    host = '192.168.10.x'
    username = 'admin'
    password = 'password'
    commands = ['display version', 'display interface description Vlanif']
    do_telnet(host, username, password, commands)
