#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
使用第三方库：pip install fabric
"""

from fabric import Connection
from paramiko import AuthenticationException


# 1. 创建一个远程连接
# 2. 查看当前目录路径
# 3. 查看当前目录有哪些文件
def do_ssh(host, username, password, commands):
    try:
        client = Connection(host=host, user=username, port=22, connect_kwargs={'password': password})
        # 执行操作
        for command in commands:
            res = client.run(command, hide=True)
            print(res.stdout)
        client.close()
    except AuthenticationException:
        print('{host} 密码错误'.format(host=host))
    except Exception as e:
        print(repr(e))


if __name__ == "__main__":
    host = '192.168.10.x'
    username = 'admin'
    password = '******'
    commands = ['pwd', 'ls']
    do_ssh(host, username, password, commands)
