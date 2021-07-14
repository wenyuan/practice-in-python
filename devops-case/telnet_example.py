#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
使用标准库：telnetlib
不建议直接在 pycharm 运行
建议用 cmd 窗口执行该函数
"""

import telnetlib
import time


# 1. 创建一个远程连接
# 2. 查看交换机查看版本信息
# 3. 查看 VLANIF 接口的状态信息、配置信息和统计信息
def do_telnet(host, username, password, commands):
    try:
        tn = telnetlib.Telnet(host, port=23, timeout=10)
    except Exception:
        print('{host} 网络连接失败'.format(host=host))
        return False

    # 输入登录用户名
    tn.read_until('Username:')
    tn.write(username + '\n')

    # 输入登录密码
    tn.read_until('Password:')
    tn.write(password + '\n')

    time.sleep(2)
    res = tn.read_very_eager()
    if 'Local authentication is rejected' in res:
        print('{host} 登录失败，用户名或密码错误'.format(host=host))
        return False

    # 登录完毕后执行命令
    for command in commands:
        tn.write(command + '\n')
        time.sleep(2)
        res = tn.read_very_eager()
        print(res)

    # 执行完毕后，终止 Telnet 连接（或输入 exit 退出）
    tn.close()


if __name__ == "__main__":
    host = '192.168.10.x'
    username = 'admin'
    password = '******'
    commands = ['display version', 'display interface description Vlanif']
    do_telnet(host, username, password, commands)
