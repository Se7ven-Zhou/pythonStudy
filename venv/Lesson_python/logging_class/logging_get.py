# coding:utf-8

import logging
import os
import time
# 1.创建一个自定义的日志收集器
logger = logging.getLogger("python_info") # 收集器的名称

# 2.自定义日志收集器手机日志的级别
logger.setLevel("INFO")  # 大写

# 3.创建一个自定义的输出渠道
sh = logging.StreamHandler()    # 控制台渠道
# fh = logging.FileHandler(filename=)     # 文件渠道
sh.setLevel("WARNING")      # 设置输出日志的级别

# 4.配套使用 自定义的日志收集器的输入渠道
# logger.addHandler(fh)

current_path = os.getcwd()
file_name = time.strftime("%Y-%m-%d_%H_%M_%S")+".txt"
file_path = os.path.join(current_path,file_name)

file = open(file_name,"w")

fh = logging.FileHandler(file_path,encoding = "utf-8")
logger.addHandler(fh)

logger.debug("debug信息")
logger.info("info信息")
logger.warning("warning信息")
logger.error("error信息")
logger.critical("critical信息")

file.close()