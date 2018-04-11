# coding:utf-8

import logging
import os
import time
# 1.创建一个自定义的日志收集器
logger = logging.getLogger("python_info") # 收集器的名称

# 2.自定义日志收集器收集日志的级别
logger.setLevel("INFO")  # 大写

# 3.创建一个自定义的输出渠道
sh = logging.StreamHandler()    # 控制台渠道
# fh = logging.FileHandler(filename=)     # 文件渠道
sh.setLevel("WARNING")      # 设置输出日志的级别

"""设置输出格式"""
"""
%(name)s        logger的名字
%(levelno)s     数字形式的日志级别
%(levelname)s   文本形式的日志级别
%(pathname)s    调用日志输出函数的模块的完整路径名
%(filename)s    调用日志输出函数的模块的文件名
%(module)s      调用日志输出函数的模块名
%(funcName)s    调用日志输出函数的函数名
%(lineno)s      调用日志输出函数的语句所在的代码行
%(created)f     当前时间，用UNIX标准的表示时间的浮点数表示
%(relativeCreated)d 输出日志信息时的，自logger创建以来的毫秒数
%(asctime)s     字符串形式的当前时间，默认格式"2013-07-07 14:45:12.777"
%(thread)d      线程ID
%(threadName)s  线程名
%(process)d     进程ID
%(message)s     用户输出信息
"""
fomatter = logging.Formatter("[%(levelName)s]-%(asctime)s-%(name)s-%(filename)s-%(funcName)s-日志信息：%(message)s")
sh.setFormatter(fomatter)   # 将格式添加到输出渠道

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

# 最后一步，使用完渠道后，记得移除渠道
logger.removeHandler(sh)
logger.removeFilter(fh)