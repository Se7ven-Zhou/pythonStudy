# coding :utf-8

import unittest
from HomeWork.unittest_0314_excel.test_http_requests import Http_requests
from HomeWork.unittest_0314_excel.read_data_by_Excel import Read_data
from HomeWork.unittest_0314_excel.test_http_requests import test_Http_requests
import time
import HTMLTestRunnerNew

# 收集测试用例

class Run:

    def Run_suite(self,data):
        suite = unittest.TestSuite()

        # 遍历测试用例
        for item in range(0,len(data)):
            url = data[item]["url"]
            tt = data[item]
            params = tt.pop("url")
            suite.addTest(test_Http_requests("test_register_excel", url, params))

        now = time.strftime("%Y-%m-%d_%H_%M_%S")  # 获取当前时间
        path = "python" + now + ".html"
        print(suite)
        with open(path, "wb+") as f:
            runner = HTMLTestRunnerNew.HTMLTestRunner(stream=f,verbosity=2,title="HttpRequests单元测试",tester="Seven")
            runner.run(suite)

if __name__ == "__main__":
    data_test = Read_data("test.xlsx").Get_data()
    Run().Run_suite(data_test)