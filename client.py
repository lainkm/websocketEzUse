#! /usr/bin/env python
# -*- coding:utf-8 -*-


import time
from websocket import create_connection
ws = create_connection("ws://39.106.190.98:8002/")
print("Sending 'Hello, World'...")
for i in range(10, 20):
    time.sleep(10)
    ws.send("Hello, World %s" % i)
    print("Sent %s"%i)
    print("Receiving...%s"%i)
    result = ws.recv()
    print("Received '%s'" % result)
time.sleep(30)
# 关闭连接
ws.close()


