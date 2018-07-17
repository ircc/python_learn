# -*- coding: utf-8 -*-

import sys
print ("脚本名：", sys.argv[0])

# 检查参数个数
if len(sys.argv) <= 2:
    print('参数输入有误, 参数个数:', len(sys.argv))
    exit()

file1=sys.argv[1]
file2=sys.argv[2]

print ("文件1：", file1, "文件2:", file2)

# 打开文件
fo=open(file1, "r")
print ("文件名为: ", fo.name)

# 按行读取文件内容
while True :   
    line=fo.readline()
    if 0==len(line):
        break
    print ("%s" % (line))



# 关闭文件
fo.close()

for i in range(1, len(sys.argv)):
    print ("参数", i, file1)