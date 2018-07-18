# -*- coding: utf-8 -*-

import sys
print ("脚本名：", sys.argv[0])

# 检查参数个数
if len(sys.argv) <= 3:
    print('参数输入有误, 参数个数:', len(sys.argv))
    exit()

file1 = sys.argv[1]
file2 = sys.argv[2]
file3 = sys.argv[3]

print ("文件1：", file1, "文件2:", file2, "文件3:", file3)

# 打开文件1
fo1=open(file1, "r")
print ("文件1名为: ", fo1.name)
file1_text = fo1.read()
fo1.close()
# 将文本按行分割存到list
file1_list_line = file1_text.split('\n')

# print(str(file1_list_line))
# 列表用于存放文件1 key主要是为了文件3写入顺序
list = []
# 字典存放 key value
dict = {}
# 将 list 的行分割并删除前后空格保存到字典中
for line in file1_list_line :
    if 0==len(line):
        continue
    # print("%s" % (line))
    spam = line.split('=')
    key = spam[0].strip()
    value = spam[1].strip()
    list.append(key)
    dict[key] = value

print(str(dict))

# 打开文件2
fo2=open(file2, "r")
print("文件2名为: ", fo2.name)
file2_text = fo2.read()
fo2.close()
# 将文本按行分割存到list
file2_list_line = file2_text.split('\n')

for line in file2_list_line :
    if 0==len(line):
        continue
    # print("%s" % (line))
    spam = line.split('=')
    key = spam[0].strip()
    if key in dict :
        value = spam[1].strip()
        dict[key] = value

print(str(dict))


# 打开文件3
fo3=open(file3, "w")

for key in list:
    fo3.write(key + '=' + dict[key]+'\n')

fo3.close()