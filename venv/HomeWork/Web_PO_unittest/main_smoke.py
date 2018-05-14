# coding:utf-8

import pytest
import time
import os


if __name__ == "__main__":

    # report_path = os.getcwd() + "/TestReports" # 测试报告地址
    #
    # now = time.strftime("%Y-%m-%d_%H_%M_%S")  # 获取当前时间
    # report_name = "python" + now + ".html"
    #
    # test_report_path = os.path.join(report_path,report_name)


    pytest.main(["-m","smoke"])