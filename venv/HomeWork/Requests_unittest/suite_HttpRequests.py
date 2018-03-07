# coding:utf-8

import unittest
from HomeWork.Requests_unittest.test_HttpRequests import Test_HttpRequests
import HTMLTestRunnerNew
import time


# 收集测试用例
"""创造测试类的实例，它是专门收集测试类的实例：方法一（addtest挨个添加）"""
# suite = unittest.TestSuite()
# suite.addTest(Test_HttpRequests("test_get_normal"))
# suite.addTest(Test_HttpRequests("test_get_abnormal"))
"""创造测试类的实例，它是专门收集测试类的实例：方法二（addtests添加成列表）"""
# suite = unittest.TestSuite()
# suite.addTests([Test_HttpRequests("test_get_normal"),Test_HttpRequests("test_get_abnormal")])
"""方法三：创造一个加载器，根据测试模块，打包收集test开头的测试用例"""
# from HomeWork.Requests_unittest import test_HttpRequests
# suite = unittest.TestSuite()
# loader = unittest.TestLoader()
# suite.addTest(loader.loadTestsFromModule(test_HttpRequests))
"""创造一个加载器，打包收集某测试类的所有test开头用例"""
suite = unittest.TestSuite()
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(Test_HttpRequests))



now = time.strftime("%Y-%m-%d_%H_%M_%S") # 获取当前时间
path = "python" + now + ".html"

# 执行用例，创造一个执行实例
with open(path,"wb+") as f:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=f, verbosity=2,title="HttpRequests单元测试",description=None,tester="Seven")
    # runner = unittest.TextTestRunner(stream=f, descriptions="测试报告", verbosity=2)
    runner.run(suite)