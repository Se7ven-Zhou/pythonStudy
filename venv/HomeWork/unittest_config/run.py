# coding :utf-8

import unittest
from HomeWork.unittest_config.http_requests import Http_requests
from HomeWork.unittest_config.read_data import Get_data
from HomeWork.unittest_config.test_http_requests import test_Http_requests
import time
import HTMLTestRunnerNew
import configparser

class Run:

    def Run_suite(self,url,data):
        suite = unittest.TestSuite()

        for item in range(0,len(data)): # 遍历用例
            params = data[item]
            suite.addTest(test_Http_requests("test_login_excel", url, params))

        now = time.strftime("%Y-%m-%d_%H_%M_%S")  # 获取当前时间
        path = "python" + now + ".html"
        data = configparser.ConfigParser()
        data.read("test.conf", encoding="utf-8")  # 读取配置文件
        api = data["ADDRESS"]["api"]
        with open(path, "wb+") as f:
            runner = HTMLTestRunnerNew.HTMLTestRunner(stream=f,verbosity=2,title= "接口自动化:"+api,tester="Seven")
            runner.run(suite)

if __name__ == "__main__":
    data_params = Get_data().Read_excel("test.xlsx")
    data_url = Get_data().Read_config("test.conf")

    Run().Run_suite(data_url,data_params)