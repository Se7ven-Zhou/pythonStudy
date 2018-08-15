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

        # 请求
        result = requests.request(data["method"],url,json=eval(data["params"]),headers=self.headers)
        Logging().Info("<请求:\t" + url +">\t<参数:" + data["params"] +">\t<结果:"+ result.text)
        # 获取报告行数
        n = WriteReport().Get_MaxRow()
        summary = "【BUG】[" + data["api"] + "]该接口状态码错误"
        description = "params:\t" + data["params"] + "\n" + "Response:\t" + result.text + "\n" + "正确状态码应该为:\t" + str(data["code"])
        try:
            assert result.json()["code"] == str(data["code"])
        except:
            # 断言错误报告
            WriteReport().Write_Report(n + 1, data["name"], data["api"], data["params"], data["code"], result.text)
            # Jira提交BUG
            KeyIssue(summary, description).Commit()
            error_info = "【断言错误】\t<正确状态码："+ str(data["code"]) +"\t<Response:\t" + result.text + ">"
            Logging().Error(error_info)
            raise

if __name__ == "__main__":

    unittest.main()
