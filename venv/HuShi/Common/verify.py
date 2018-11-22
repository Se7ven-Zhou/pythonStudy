# coding:utf-8

import requests
import urllib3
from HuShi.Common.readData import Read_Data
from HuShi.Common.readData_DDT import Read_Data_ddt
from HuShi.Common.logger import Logging
from HuShi.Common.package_params import Parameter
from HuShi.Config.env_config import Environment
from HuShi.Common.writeReport import WriteReport
from HuShi.Common.keyIssue import KeyIssue
from HuShi.Common.conn_mysql import Conn_MySQL
from HuShi.Common.sendMail import Send_Mail
from HuShi.Common.getLatestReport import GetLatestReport
import HuShi.Config.params_config,HuShi.Config.testData_config
import unittest
import os,time


class Verify:

    def __init__(self, data, result,n):

        self.data = data
        self.result = result
        self.n = n

    def VerifyValue(self):
        # 链接数据库，查询比对数据
        SQL_check_data = Conn_MySQL().Connect(self.data["SQL_check"])
        try:
            assert str(self.data["check_data"]) == str(SQL_check_self.data["result"])
        except:
            WriteReport().Write_Report(self.n + 1, self.data["name"], self.data["api"], self.data["params"],
                                       str(SQL_check_self.data), self.result.text)
            # Jira提交BUG
            # KeyIssue().Commit(self.data["api"],self.data["params"],self.result.text,str(check_self.data),1,sql=self.data["check"])
            error_info = "【断言错误】\t<验证值：" + str(SQL_check_self.data) + "\t<Response:\t" + self.result.text + ">"
            Logging().Error(error_info)
            raise

    def Verifydata(self):
        # 链接数据库，查询比对数据
        SQL_check_data = Conn_MySQL().Connect(self.data["SQL_check"])
        try:
            assert str(SQL_check_self.data["result"]) == str(
                self.result.json()["result"][self.data["check_data"]])
        except:
            WriteReport().Write_Report(self.n + 1, self.data["name"], self.data["api"], self.data["params"],
                                       str(SQL_check_self.data),
                                       self.result.text)
            # Jira提交BUG
            # KeyIssue().Commit(self.data["api"],self.data["params"],self.result.text,str(check_self.data),1,sql=self.data["check"])
            error_info = "【断言错误】\t<验证值：" + str(SQL_check_self.data) + "\t<Response:\t" + self.result.text + ">"
            Logging().Error(error_info)
            raise


    def VerifydataExist(self):
        # 链接数据库，查询比对数据
        SQL_check_data = Conn_MySQL().Connect(self.data["SQL_check"])
        try:
            # 传值当前时间，用于比对
            self.data["check_data"] = now
            assert str(self.data["check_data"]) == str(SQL_check_self.data["result"])
        except:
            WriteReport().Write_Report(self.n + 1, self.data["name"], self.data["api"], self.data["params"],
                                       str(SQL_check_self.data), self.result.text)
            # Jira提交BUG
            # KeyIssue().Commit(self.data["api"],self.data["params"],self.result.text,str(check_self.data),1,sql=self.data["check"])
            error_info = "【断言错误】\t<验证值：" + str(SQL_check_self.data) + "\t<Response:\t" + self.result.text + ">"
            Logging().Error(error_info)
            raise


    def VerifyCode(self):
        try:
            assert self.result.json()["code"] == str(self.data["code"])
        except:
            # 断言错误报告
            WriteReport().Write_Report(self.n + 1, self.data["name"], self.data["api"], self.data["params"], self.data["code"],
                                       self.result.text)
            # Jira提交BUG
            # KeyIssue().Commit(self.data["api"], self.data["params"], self.result.text, self.data["code"], 0)
            error_info = "【断言错误】\t<正确状态码：" + str(self.data["code"]) + "\t<Response:\t" + self.result.text + ">"
            Logging().Error(error_info)
            raise