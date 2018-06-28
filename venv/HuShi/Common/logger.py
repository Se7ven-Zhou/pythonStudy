# coding:utf-8

import logging
import os
import time


class Logging:

    def __init__(self):

        self.address = os.path.split(os.getcwd())[0] + "\Logs"
        self.log_name = time.strftime("%Y-%m-%d")+".txt"
        self.log_path = os.path.join(self.address,self.log_name)

        # 生成日志文件,日期命名，没有就创建
        if os.path.exists(self.log_path):
            file = open(self.log_path, "a")
            file.close()
        else:
            file = open(self.log_path, "w")
            file.close()


    def Get_Error(self,message):

        logger = logging.getLogger("Interface_Auto_Error")  # 创建日志收集器
        fh = logging.FileHandler(self.log_path, encoding="utf-8")  # 创建日志输出渠道
        logger.addHandler(fh)  # 收集器添加输出渠道
        # 创建输出格式
        formatter = logging.Formatter("[%(levelname)s]-[%(asctime)s]-[%(filename)s]-[%(module)s]-[%(funcName)s]--日志信息：%(message)s")
        fh.setFormatter(formatter)

        logger.error(message) # 输出内容
        logger.removeFilter(fh)


    def Get_Info(self,message):

        logger = logging.getLogger("Interface_Auto_Info")  # 创建日志收集器
        fh = logging.FileHandler(self.log_path, encoding="utf-8")  # 创建日志输出渠道
        logger.addHandler(fh)  # 收集器添加输出渠道
        # 创建输出格式
        formatter = logging.Formatter("[%(levelname)s]-[%(asctime)s]-[%(filename)s]-[%(module)s]-[%(funcName)s]--日志信息：%(message)s")
        fh.setFormatter(formatter)

        logger.info(message) # 输出内容
        logger.removeFilter(fh)


if __name__ == "__main__":

    Logging().Get_Info("bbb")
    # try:
    #     aaaa
    # except Exception as error:
    #     Logging().Get_Error(error)
    #     raise