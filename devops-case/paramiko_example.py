#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
使用第三方库：paramiko
"""

import paramiko
from paramiko.ssh_exception import NoValidConnectionsError
from paramiko.ssh_exception import AuthenticationException


def do_ssh(host, username, password, commands):
    client = paramiko.SSHClient()
    # 如果是之前没有连接过的 ip，会出现选择 yes 或者 no 的操作
    # 自动选择 yes
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(hostname=host, port=22, username=username, password=password)
    except NoValidConnectionsError:
        print('{host} 无法连接'.format(host=host))
    except AuthenticationException:
        print('{host} 密码错误'.format(host=host))
    except Exception as e:
        print(repr(e))
    else:
        # 执行操作
        for command in commands:
            stdin, stdout, stderr = client.exec_command(command)
            # 获取命令执行的结果
            for line in stdout:
                print(line.strip('\n'))
    finally:
        # 关闭连接
        client.close()


if __name__ == "__main__":
    host = '192.168.10.x'
    username = 'admin'
    password = 'password'
    commands = ['hostname', 'ls']
    do_ssh(host, username, password, commands)
