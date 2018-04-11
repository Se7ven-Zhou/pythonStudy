# coding:utf-8

import os
import time
import logging

class Logging_class:

    def logging_connect(self,message):
        """日志文件信息"""
        current_path = os.getcwd()
        file_name = time.strftime("%Y-%m-%d")+".txt"
        file_path = os.path.join(current_path,file_name)

        """日志收集器信息"""
        logger = logging.getLogger("UnitTest")  # 创建收集器
        fh = logging.FileHandler(file_path,encoding = "utf-8")    # 创建输出渠道
        logger.addHandler(fh)  # 收集器添加输出渠道，连接
        fomatter = logging.Formatter("[%(levelname)s]-[%(asctime)s]-[%(name)s]-[%(filename)s]-[%(funcName)s]-日志信息：%(message)s")
        fh.setFormatter(fomatter)  # 设置的输出格式
        fh.setLevel("ERROR")

        """创建日志文件,日期命名，有就写，没有就创建写"""
        if os.path.exists(file_path):
            file = open(file_path, "a")
            file.close()
        else:
            file = open(file_path, "w")
            file.close()

        logger.error(message)
        logger.removeFilter(fh)

if __name__ == "__main__":
    try:
        a
    except Exception as error:
        log = Logging_class().logging_connect(error)
