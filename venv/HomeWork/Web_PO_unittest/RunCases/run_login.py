# coding:utf-8

import time
import os
import unittest
import HTMLTestRunnerNew
from selenium import webdriver
from HomeWork.Web_PO_unittest.PageObjects import login_page
from HomeWork.Web_PO_unittest.PageObjects import index_page
from HomeWork.Web_PO_unittest.TestDatas.read_datas import Read_data
from HomeWork.Web_PO_unittest.TestCases.test_login import Login_test


class Run_Cases:

    def __init__(self):
        pass

    def Run_login(self,file_name):

        # 收集测试用例
        suite = unittest.TestSuite()

        # 获取测试数据
        success_data = Read_data(file_name).Read_login_success("login_success")
        # 遍历测试用例
        for item in range(0,len(success_data)):
            suite.addTest(Login_test("test_login_success",success_data[item]))

        # 生成报告
        now = time.strftime("%Y-%m-%d_%H_%M_%S")  # 获取当前时间
        report_name = "python" + now + ".html"

        with open(report_name, "wb+") as f:
            runner = HTMLTestRunnerNew.HTMLTestRunner(stream=f,verbosity=2,title="HttpRequests单元测试",tester="Seven")
            runner.run(suite)

if __name__ == "__main__":

    Run_Cases().Run_login("Login_Data.xlsx")



