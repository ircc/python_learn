#SyncLocaltime.py
# -*- coding: utf-8 -*-

# import urllib
import requests
import json
import re
import os
import datetime
import time
# import win32serviceutil
# import win32service
# import win32event
# import win32evtlogutil

# 阿里获取时间的域名 这里返回的是毫秒级时间戳
url = "http://api.m.taobao.com/rest/api3.do?api=mtop.common.getTimestamp"

# 苏宁获取时间接口
# http://quan.suning.com/getSysTime.do
# qq获取日间接口
# http://cgi.im.qq.com/cgi-bin/cgi_svrtime

# 通过指定域名获取当前时间的时间戳
def get_information(url):
    try:
        ret = requests.get(url) 
        print(ret.text)
    except :
        print("打开失败" + ret.status_code)
        return [] 
    if 200 != ret.status_code:
        return [] 

    print ("ret.text: ", ret.text)
    # 将json字符串转成字典
    dict = json.loads(ret.text)
    timemap = dict['data']['t']
    return timemap

def get_time():
    ans = [] 
    while True :
        ch = get_information( url );
        print(ch)
        if len(ch) == 0 :
            print ("30秒后将重新连接")
            time.sleep( 30 ) 
        else :
            break; 
        print(ch)
        
        timearr = time.localtime(int(ch))
        otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timearr)
        print (otherStyleTime)

    for i in range(1 , len( ch )-1 ):
        ss = re.search( r'\d' , ch[i] ).start()
        needed = ch[i][ss : len( ch[i] ) ]
        ans.append( int(needed) )
    os.system("date %d-%d-%d" % ( ans[0] , ans[1] , ans[2]) )
    os.system("time %d:%d:%d.0" % ( ans[4] , ans[5] ,ans[6]) )
    date = str(ans[0])
    print(date)

# 节假日判断接口
# http://api.goseek.cn/
# http://tool.bitefu.net/jiari/
if __name__=='__main__':
    print(url)
    get_time()
