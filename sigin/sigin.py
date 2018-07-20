#SyncLocaltime.py
# -*- coding: utf-8 -*-

from check_time import check_time

if __name__ == '__main__':
    t = check_time()
    print(t.get_today_date())
    print(t.get_cur_time())
    ret = t.is_holiday()
    print("工作日对应结果为 0, 休息日对应结果为 1, 节假日对应的结果为 2;返回结果:" + str(ret))
