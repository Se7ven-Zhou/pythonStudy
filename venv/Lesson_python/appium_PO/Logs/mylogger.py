# coding:utf-8

import logging
import time
import os

class Logging:

    def __init__(self):
        pass

    def My_logger(self,message):

        # 日志存储信息
        address = os.path.dirname(__file__)
        log_name ="/" + time.strftime("%Y-%m-%d")+".txt"
        log_path = os.path.join(address + log_name)
        # 创建日志收集器
        logger = logging.getLogger("Web_Auto")  # 创建日志收集器
        fh = logging.FileHandler(log_path,encoding="utf-8")     # 创建日志输出渠道
        logger.addHandler(fh)   # 收集器添加输出渠道
        # 设置日志输出格式
        formatter = logging.Formatter("[%(levelname)s]-[%(asctime)s]-[%(name)s]-[%(filename)s]-[%(funcName)s]-日志信息：%(message)s")
        fh.setFormatter(formatter)
        # fh.setLevel(level)

        logger.error(message)
        logger.removeFilter(fh)

        # 生成日志文件,日期命名，没有就创建
        if os.path.exists(log_path):
            file = open(log_path, "a")
            file.close()
        else:
            file = open(log_path, "w")
            file.close()

if __name__ == "__main__":

    try:
        a
    except Exception as error:
        Logging().My_logger(error)
        raise