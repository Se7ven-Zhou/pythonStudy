# coding:utf-8

import unittest
from HomeWork.unittest_0313.test_http_requests import Test_HttpRequests
from HomeWork.unittest_0313.read_data import Read_data
import time
import HTMLTestRunnerNew

class Run:

    def __init__(self,data):
        self.data = data

    def Run_case(self):
        suite = unittest.TestSuite()    # 实例测试集
        for item in range(0,len(self.data)):
            mobile = self.data[item]["mobilephone"]
            pwd = self.data[item]["pwd"]
            suite.addTest(Test_HttpRequests("test_register",mobile,pwd))    # 收集测试用例

        now = time.strftime("%Y-%m-%d_%H_%M_%S") # 获取当前时间
        path = "python" + now + ".html"

        with open(path,"wb+") as f:
            runner = HTMLTestRunnerNew.HTMLTestRunner(stream=f, verbosity=2,title="HttpRequests单元测试",description=None,tester="Seven")
            runner.run(suite)

if __name__ == "__main__":
    data = Read_data("data_test.txt").get_data()
    Run(data).Run_case()
