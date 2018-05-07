# coding:utf-8

import logging
import os
import time

"""取文件信息"""
current_path = os.getcwd()
file_name = time.strftime("%Y-%m-%d")+".txt"
file_path = os.path.join(current_path,file_name)
"""日志信息"""
logger = logging.getLogger("python_info")
fh = logging.FileHandler(file_path,encoding = "utf-8")
logger.addHandler(fh)
# logger.critical("崩溃信息")


if os.path.exists(file_path):
    file = open(file_path,"a")
    logger.addFilter(fh)
    file.close()
else:
    file = open(file_path,"w")
    logger.addFilter(fh)
    file.close()

logger.critical("崩溃信息")
