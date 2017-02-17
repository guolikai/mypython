#!/usr/bin/env python
# -*- coding: utf8 -*-

import subprocess  # 该模块用于调用系统命令
import threading

def ping(ip):
    result = subprocess.call(
        'ping -c2 %s &> /dev/null' % ip, shell=True
    )  # result的结果是ping的退出码
    if result == 0:
        print "%s:up" % ip
    else:
        print "%s:down" % ip

if __name__ == '__main__':
    ips = ["172.40.53.%s" % i for i in range(1, 255)]
    for ipaddr in ips:
        t = threading.Thread(target=ping, args=[ipaddr])
        t.start()
