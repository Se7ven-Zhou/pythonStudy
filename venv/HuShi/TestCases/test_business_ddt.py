# coding:utf-8

import requests
from HuShi.Common.readData import Read_Data
from HuShi.Common.readData_DDT import Read_Data_ddt
from HuShi.Common.logger import Logging
from HuShi.Common.package_params import Parameter
from HuShi.Config.env_config import Environment
from HuShi.Common.writeReport import WriteReport
from HuShi.Common.keyIssue import KeyIssue
import HuShi.Config.params_config
import unittest
import os
import time
import ddt
#
# data_ddt = Read_Data_ddt("test_data_ddt.xlsx").Get_Data()
#
# @ddt.ddt
# class test_Requests(unittest.TestCase):
#
#     def __init__(self,method):
#         super(test_Requests, self).__init__(method)
#         self.headers = HuShi.Config.params_config.headers
#
#     @ddt.data(*data_ddt)
#     def test_requests(self,data):
#
#         WriteReport().Creat_Report()
#         url = Environment().Test() + data["api"]
#
#         try:
#             # 请求
#             result = requests.request(data["method"],url,json=eval(data["params"]),headers=self.headers)
#             Logging().Info("< Request:" + url + " >< Parameters:" + data["params"] +" >< Respose: "+ str(result.json()))
#             # 获取报告行数
#             n = WriteReport().Get_MaxRow()
#             # 构建提交BUG内容
#             summary = "【BUG】[" + data["api"] + "]该接口状态码错误"
#             description = "params:\t" + data["params"] + "\n" + "Response:\t" + result.text + "\n" + "正确状态码应该为:\t" + str(data["code"])
#             # 断言状态码，错误就写报告并提交
#             assert int(result.json()["code"]) == data["code"],KeyIssue(summary,description).Commit() and WriteReport().Write_Report(n+1,data["name"], data["api"], data["params"], data["code"],str(result.json()))
#         except Exception as error:
#             error_info = "<AssertionError> " + str(result.json()["code"]) + "≠" + str(data["code"]) + " <Response:" + str(result.json()) + ">"
#             WriteReport().Write_Report(n + 1, data["name"], data["api"], data["params"], data["code"],str(result.text))
#             Logging().Error(error_info)
#             Logging().Error(error)
#             raise error


data_ddt = Read_Data_ddt("test_data_ddt.xlsx").Get_Data()

@ddt.ddt
class test_Requests(unittest.TestCase):

    def __init__(self,method):
        super(test_Requests, self).__init__(method)
        self.headers = HuShi.Config.params_config.headers

    @ddt.data(*data_ddt)
    def test_requests(self,data):

        WriteReport().Creat_Report()
        url = Environment().Test() + data["api"]

        try:
            # 请求
            result = requests.request(data["method"],url,json=eval(data["params"]),headers=self.headers)
            Logging().Info("< Request:\t" + url + " >< Parameters:\t" + data["params"] +" >< Respose:\t"+ str(result.json()))
            # 获取报告行数
            n = WriteReport().Get_MaxRow()
            assert int(result.json()["code"]) == data["code"], WriteReport().Write_Report(n + 1, data["name"],data["api"], data["params"],data["code"],str(result.json()))

        except Exception as error:
            error_info = "<AssertionError> " + str(result.json()["code"]) + "≠" + str(data["code"]) + " <Response:\t" + str(result.json()) + ">"
            WriteReport().Write_Report(n + 1, data["name"], data["api"], data["params"], data["code"], str(result.text))
            Logging().Error(error_info)
            raise error

            # 构建提交BUG内容
            summary = "【BUG】[" + data["api"] + "]该接口状态码错误"
            description = "params:\t" + data["params"] + "\n" + "Response:\t" + result.text + "\n" + "正确状态码应该为:\t" + str(data["code"])
            # 断言状态码，错误就写报告并提交
            # assert int(result.json()["code"]) == data["code"],KeyIssue(summary,description).Commit() and WriteReport().Write_Report(n+1,data["name"], data["api"], data["params"], data["code"],str(result.json()))


if __name__ == "__main__":

    unittest.main()
