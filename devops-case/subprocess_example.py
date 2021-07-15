#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
使用标准库：subprocess
建议在 Linux 环境执行
"""

import subprocess
import sys
import time


# 1. 不等待子进程
def exec_without_block():
    # 或者：child = subprocess.Popen(['ping', '-c', '4', 'www.baidu.com'])
    child = subprocess.Popen(['ping -c 4 www.baidu.com'], shell=True)
    print(child)
    print('hello world')


# 2. 等待子进程（阻塞）
def exec_with_block():
    child = subprocess.Popen(['ping -c 4 www.baidu.com'], shell=True)
    child.wait()
    print(child)
    print('hello world')


# 3. 获取命令执行结果
def get_exec_result():
    child = subprocess.Popen(['cat /etc/issue'],
                             shell=True,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
    child.wait()
    result = child.stdout.read()
    if not result:
        err = child.stderr.read()
        print(sys.stderr, 'ERROR: %s' % err)
    else:
        print(result)


if __name__ == "__main__":
    get_exec_result()
