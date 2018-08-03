# coding:utf-8

import requests
from HuShi.Common.readData import Read_Data
from HuShi.Common.readData_DDT import Read_Data_ddt
from HuShi.Common.logger import Logging
from HuShi.Common.package_params import Parameter
from HuShi.Config.env_config import Environment
from HuShi.Common.writeReport import WriteReport
import HuShi.Config.params_config
import unittest
import os
import time
import ddt

data_ddt = Read_Data_ddt("test_data_ddt.xlsx").Get_Data()

@ddt.ddt
class Requests(unittest.TestCase):

    def __init__(self,method):
        super(Requests, self).__init__(method)

        self.signature = HuShi.Config.params_config.signature
        self.token = HuShi.Config.params_config.token
        self.headers = HuShi.Config.params_config.headers

    @ddt.data(*data_ddt)
    def test_Requests(self,data):
        n=1
        n+=1
        params = Parameter().Package_params(data["params"], signature=self.signature)
        url = Environment().Test() + data["api"]
        # 请求
        result = requests.request(data["method"],url,params=params,headers=self.headers)
        Logging().Info("Request:" + url + "  Parameters:" + str(params))
        assert int(result.json()["code"]) == data["code"], WriteReport().Write_Report(data["name"], data["api"], data["params"], data["code"],str(result.json()))
        # except Exception as error:
        #     error_info = "<AssertionError> " + str(result.json()["code"]) + "≠" + str(code_list[item]) + " <Response:" + str(result.json()) + ">"
        #     Logging().Error(error_info)
        #     raise error

if __name__ == "__main__":

    unittest.main()