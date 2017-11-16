#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import redis

devNum = 0
userNum = 0

def handle_key(r2, key2):
    global userNum
    filedNum = r2.hlen(key2)
    if filedNum > 0:
        userNum = userNum + 1
    return filedNum

def handle_keys(r1, keys):
    global devNum
    for key1 in keys:     # 第一个实例
        if len(key1):
            devNum = devNum + handle_key(r1, key1)
            print('key :', key1)


count = 0
while(count<256):
    # print("into db:", count)
    # r = redis.Redis(host='r-bp171003b4510ea4.redis.rds.aliyuncs.com', port=6379, db=count, password='eteamsProducte681')
    r = redis.Redis(host='r-bp14d30917f265d4.redis.rds.aliyuncs.com', port=6379, db=count, password='eteamsBeta123')
    u_keys = r.keys('u_*')
    handle_keys(r, u_keys)
    count = count + 1

print("userNum:", userNum, "devNum:", devNum)