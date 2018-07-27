# coding:utf-8

import time
import os
import HTMLTestRunnerNew
from HomeWork.Appium_Video.TestCases.test_login import Test_login
import unittest

if __name__ == "__main__":

    suite = unittest.TestSuite()
    loader = unittest.TestLoader()

    testcase_path = os.getcwd() + "/TestCases" # 测试用例路径
    suite.addTest(loader.discover(testcase_path))  # 加载目录下以test开头的py文件

    now = time.strftime("%Y-%m-%d_%H_%M_%S")  # 获取当前时间
    report_name = "python" + now + ".html"
    report_filepath = os.getcwd() + "/Report"
    report_path = os.path.join(report_filepath,report_name)

    with open(report_path, "wb+") as f:
        runner = HTMLTestRunnerNew.HTMLTestRunner(stream=f, verbosity=2, title="Appium Android Autotest", tester="Seven")
        runner.run(suite)
