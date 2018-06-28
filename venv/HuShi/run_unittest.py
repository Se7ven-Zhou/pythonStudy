# coding:utf-8

import os
import time
import unittest
import HuShi.Config.params_config
import HTMLTestRunnerNew
from HuShi.Config.env_config import Environment
from HuShi.Common.logger import Logging
from HuShi.TestCases.test_CollectVideo import test_Collect_Video



if __name__ == "__main__":

    suite = unittest.TestSuite
    loader = unittest.TestLoader

    testcase_path = os.getcwd() + "/TestCases" # 测试用例路径
    suite.addTest(loader.discover(testcase_path))  # 加载目录下以test开头的py文件

    now = time.strftime("%Y-%m-%d_%H_%M_%S")  # 获取当前时间
    report_name = "<python_unittest>" + now + ".html"

    with open(report_name, "wb+") as f:
        runner = HTMLTestRunnerNew.HTMLTestRunner(stream=f, verbosity=2, title="Requests_AutoTest", tester="Seven")
        runner.run(suite)