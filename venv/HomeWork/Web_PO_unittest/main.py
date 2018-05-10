# coding:utf-8

import os
import unittest
import HTMLTestRunnerNew
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
    suite.addTests(loader.discover(testcase_path))  # 加载目录下以test开头的py文件