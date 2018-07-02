# coding:utf-8

import os
import time
import unittest
import HuShi.Config.params_config
import HTMLTestRunnerNew
from HuShi.Config.env_config import Environment
from HuShi.Common.logger import Logging
from HuShi.TestCases.test_searchMeeting import test_SearchMeeting
from HuShi.TestCases import test_searchMeeting

if __name__ == "__main__":

    suite = unittest.TestSuite
    loader = unittest.TestLoader

    testcase_path = os.getcwd() + "/TestCases" # 测试用例路径
    # suite.addTest(test_SearchMeeting("test_Search_Meeting_Normal"))  # 加载目录下以test开头的py文件
    #suite.addTests(loader.loadTestsFromTestCase(test_SearchMeeting))
    #suite.addTest(loader.loadTestsFromModule(test_searchMeeting))
    suite.addTest(test_SearchMeeting("test_Search_Meeting_Normal"))

    now = time.strftime("%Y-%m-%d_%H_%M_%S")  # 获取当前时间
    report_name = "<python_unittest>" + now + ".html"
    print(suite)
    # with open(report_name, "wb+") as f:
    #     runner = HTMLTestRunnerNew.HTMLTestRunner(stream=f, verbosity=2, title="Requests_AutoTest", tester="Seven")
    #     runner.run(suite)