#coding:utf-8

"""
r ： 文件只读模式，光标放在最前头
r+ ：从头写，后面内容会被覆盖
w ： 文件只能写，内容会被重写
w+ ：内容会被覆盖，如果不存在会新建一个文件
a ： 追加写入（在末尾写），如果不存在会新建一个文件
"""

"""
read(count) 传几就读几个（是几个位置，不是几个字符），不传默认读全部内容，指针会在读完的地方
tell() 查看光标位置（字符）
seek(位移数，相对位置) 指针偏移（0是开头，1是当前位置，2是最后）
"""

file = open("D:\\Python27\\Case\\Test\\zj.txt",'a+')
# print file.readlines()
# file.write("456")
# file.seek(0,0)
# print(file.tell())

for item in file:
    print item

file.close()