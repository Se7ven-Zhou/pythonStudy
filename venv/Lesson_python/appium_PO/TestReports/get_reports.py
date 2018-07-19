# coding:utf-8

import os
import time
import HTMLTestRunnerNew


class Get_report:

    def __init__(self):

       pass

    def Report(self):
        address = os.path.dirname(__file__)
        now = time.strftime("%Y-%m-%d_%H_%M_%S")  # 获取当前时间
        report_name = "python" + now + ".html"
        report_path = os.path.join(address, report_name)

        with open(report_path, "wb+") as f:
            runner = HTMLTestRunnerNew.HTMLTestRunner(stream=f, verbosity=2, title="HttpRequests单元测试", tester="Seven")
            runner.run(suite)