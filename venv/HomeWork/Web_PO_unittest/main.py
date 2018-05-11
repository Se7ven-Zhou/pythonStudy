# coding:utf-8

import os
import unittest
import HTMLTestRunnerNew
import time
from selenium import webdriver
from HomeWork.Web_PO_unittest.PageObjects import login_page
from HomeWork.Web_PO_unittest.PageObjects import index_page
from HomeWork.Web_PO_unittest.TestDatas.read_datas import Read_data
from HomeWork.Web_PO_unittest.TestCases.test_login import Login_test
from HomeWork.Web_PO_unittest.TestReports.get_reports import Get_report


if __name__ == "__main__":

    suite = unittest.TestSuite
    loader = unittest.TestLoader

    testcase_path = os.getcwd() + "/TestCases" # 测试用例路径
    suite.addTest(loader.discover(testcase_path))  # 加载目录下以test开头的py文件
    discover = unittest.defaultTestLoader.discover(testcase_path, pattern='test*.py')

    print(discover)
    now = time.strftime("%Y-%m-%d_%H_%M_%S")  # 获取当前时间
    report_name = "python" + now + ".html"

    with open(report_name, "wb+") as f:
        runner = HTMLTestRunnerNew.HTMLTestRunner(stream=f, verbosity=2, title="HttpRequests单元测试", tester="Seven")
        runner.run(suite)
