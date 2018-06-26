# coding:utf-8

import requests
from HuShi.Common.readData import Read_Data
from HuShi.Common.logger import Logging
from HuShi.Common.package_params import Parameter
from HuShi.Config.env_config import Environment
import HuShi.Config.params_config


class Collect_Video:

    def __init__(self):

        self.api = "/meeting/search"

    def test_Search_Meeting_Normal(self):
        # 登录信息
        signature = HuShi.Config.params_config.signature
        token = HuShi.Config.params_config.token
        params_dict = {"searchKey":"笑话","pageNo":1,"pageSize":20}
        headers = HuShi.Config.params_config.headers

        params = Parameter().Package_params(str(params_dict),token,signature)
        url = Environment().Test() + self.api
        try:
            result = requests.post(url,params,headers = headers)
            assert result.json()["code"] == "0"
        except Exception as error:
            info = "AssertionError - " + str(result.json())
            Logging().Get_Error(info)
            raise error


    def test_Search_Meeting_NoContent(self):
        headers = HuShi.Config.params_config.headers
        params_dict = {"searchKey":"","pageNo":1,"pageSize":20}

        params = Parameter().Package_params(str(params_dict))
        url = Environment().Test() + self.api
        result = requests.post(url,params,headers = headers)
        print(result.json())

if __name__ == "__main__":

    Collect_Video().test_Search_Meeting_Normal()
