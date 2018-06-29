# coding:utf-8

import requests
from HuShi.Common.readData import Read_Data
from HuShi.Common.logger import Logging
from HuShi.Common.package_params import Parameter
from HuShi.Config.env_config import Environment
import HuShi.Config.params_config
import pytest
import os
import time


class test_Collect_Video:

    def __init__(self):

        self.api = "/meeting/search"
        self.signature = HuShi.Config.params_config.signature
        self.token = HuShi.Config.params_config.token
        self.headers = HuShi.Config.params_config.headers


    def test_Search_Meeting_Normal(self):
        params_dict = {"searchKey":"笑话","pageNo":1,"pageSize":20}

        params = Parameter().Package_params(str(params_dict),self.token,self.signature)
        url = Environment().Test() + self.api
        try:
            result = requests.post(url,params,headers = self.headers)
            assert result.json()["code"] == "520"
        except Exception as error:
            info = "AssertionError - " + str(result.json())
            Logging().Get_Error(info)
            raise error


    def test_Search_Meeting_NoContent(self):
        params_dict = {"searchKey":"","pageNo":1,"pageSize":20}
        try:
            params = Parameter().Package_params(str(params_dict),signature=self.signature)
            url = Environment().Test() + self.api
            result = requests.post(url,params,headers = self.headers)
            Logging().Info("Request:"+ url + "  Parameters:"+ str(params))
            assert result.json()["code"] == "2000022"
        except Exception as error:
            error_info = "<AssertionError> " + str(result.json()["code"]) + "≠ 2000022, Response:" + str(result.json())
            Logging().Error(error_info)
            raise error

if __name__ == "__main__":
    test_Collect_Video().test_Search_Meeting_NoContent()
