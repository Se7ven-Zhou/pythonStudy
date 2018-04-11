# coding:utf-8

import logging
import os
import time

"""取文件信息"""
current_path = os.getcwd()
file_name = time.strftime("%Y-%m-%d")+".txt"
file_path = os.path.join(current_path,file_name)
"""日志信息"""
logger = logging.getLogger("python_info")   #  创建收集器
fh = logging.FileHandler(file_path,encoding = "utf-8")  # 创建输出渠道
logger.addHandler(fh)   # 添加输出渠道
fomatter = logging.Formatter("[%(levelname)s]-[%(asctime)s]-[%(name)s]-[%(filename)s]-[%(funcName)s]-日志信息：%(message)s")
fh.setFormatter(fomatter)   # 设置输出渠道格式
fh.setLevel("ERROR")    # 设置输出日志级别

if os.path.exists(file_path):
    file = open(file_path,"a")
    file.close()
else:
    file = open(file_path,"w")
    file.close()

logger.critical("崩溃信息")