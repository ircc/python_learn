# gettime.py
# -*- coding: utf-8 -*-

import requests
import json
# import os
# import datetime

# 通过web接口获取准确的时间


# 苏宁获取时间接口 {"sysTime1":"20180720161634","sysTime2":"2018-07-20 16:16:34"}
url_sn = "http://quan.suning.com/getSysTime.do"
# qq获取日间接口 2018-07-20 16:17:04
url_qq = "http://cgi.im.qq.com/cgi-bin/cgi_svrtime"
# 阿里获取时间的域名 这里返回的是毫秒级时间戳 {"api":"mtop.common.getTimestamp","v":"*","ret":["SUCCESS::接口调用成功"],"data":{"t":"1532074649625"}}
url_tb = "http://api.m.taobao.com/rest/api3.do?api=mtop.common.getTimestamp"


# 节假日判断接口
# http://api.goseek.cn/
# http://tool.bitefu.net/jiari/
# 检查是否为节假日 {"code":10000,"data":2} 工作日对应结果为 0, 休息日对应结果为 1, 节假日对应的结果为 2
url_check_holiday = "http://api.goseek.cn/Tools/holiday?date="

# 通过指定域名url_sn获取当前时间的时间戳
def get_time_by_sn():
    try:
        ret = requests.get(url_sn)
        print(ret.text)
    except:
        print("打开失败" + ret.status_code)
        return []
    if 200 != ret.status_code:
        return []

    print("ret.text: ", ret.text)
    # 将json字符串转成字典
    dict = json.loads(ret.text)
    sysTime = dict['sysTime1']
    date = sysTime[0:8]
    time = sysTime[8:]
    return date, time


class check_time:
    # constructor 初始化获取时间
    def __init__(self):
        self.date, self.time = get_time_by_sn()

    # member function 获取今天日期
    def get_today_date(self):
        return self.date

    # member function 获取当前时间
    def get_cur_time(self):
        return self.time

    def is_holiday(self):
        url = url_check_holiday + self.date
        try:
            ret = requests.get(url)
        except:
            print("打开失败" + ret.status_code)
            return []
        if 200 != ret.status_code:
            return []

        # 将json字符串转成字典
        dict = json.loads(ret.text)
        ret = dict['data']
        return ret


# if __name__ == '__main__':
#     print(url_tb)
#     t = CheckTime()
#     print(t.get_today_date())
#     print(t.get_cur_time())
#     ret = t.is_holiday()
#     print("工作日对应结果为 0, 休息日对应结果为 1, 节假日对应的结果为 2;返回结果:" + str(ret))
