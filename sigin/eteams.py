#SyncLocaltime.py
# -*- coding: utf-8 -*-
import requests
import json
import os
import time

url_login = "https://www.eteams.cn/teamsLogin"
url_logout = "https://www.eteams.cn/teamsLogout"
url_check = "https://www.eteams.cn/timecard/check.json"
url_checks = "https://www.eteams.cn/app/timecard/checks.json"


class eteams_sigin:
        # constructor 初始化获取时间
    def __init__(self, name, pwd):
        self.name = name
        self.pwd = pwd
        self.uid = ""
        self.jsessionid = ""
        self.etemsid = ""
    
    def login(self):
        data = {"username":self.name, "password":self.pwd, "client":"android", "version":"3.6.91"}
        ret = requests.post(url_login, data)
        if 200 != ret.status_code:
            print("登陆失败 status_code：", ret.status_code)
            return []
        print("登录成功, ret.text: ", ret.text)
        # 将json字符串转成字典
        dict = json.loads(ret.text)
        self.uid = dict['uid']
        self.jsessionid = dict['jsessionid']
        self.etemsid = dict["ETEAMSID"]
        print('uid:', self.uid, ' jsessionid:', self.jsessionid)
        # return date, time


    def logout(self):
        data = {"jsessionid":self.jsessionid}
        ret = requests.post(url_logout, data)
        if 200 != ret.status_code:
            print("登出失败 status_code：", ret.status_code, "data:", data)
            return []
        print("登出成功 !!!")  


    def get_checks(self):
        data = {"ETEAMSID":self.etemsid, "jsessionid":self.jsessionid, "employeeId":self.uid, "date":time.strftime("%Y-%m-%d %H:%M:%S")}
        print(data)
        ret = requests.post(url_checks, data)
        if 200 != ret.status_code:
            print("checks失败 status_code：", ret.status_code)
            return []        
        print("checks成功, ret.text: ", ret.text)

    def check_in(self, is_in):
        data = {"ETEAMSID":self.etemsid, "jsessionid":self.jsessionid, "userId":self.uid}
        if is_in:
            data["type"] = "CHECKIN"            
            data["longitude"] = "121.532931"
            data["latitude"] = "31.085895"
            data["checkAddress"] = "泛微软件大厦"
        else:
            data["type"] = "CHECKOUT"
        print(data)
        ret = requests.post(url_check, data)
        if 200 != ret.status_code:
            print("checks失败 status_code：", ret.status_code)
            return []        
        print("checks成功, ret.text: ", ret.text)


if __name__ == '__main__':
    t = eteams_sigin('r1@im.com', '111111')
    t.login()
    time.sleep(1) # 休眠1秒
    # t.get_checks()
    t.check_in(False)
    time.sleep(1) # 休眠1秒
    t.logout()