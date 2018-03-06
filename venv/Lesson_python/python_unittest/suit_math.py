# coding:utf-8

# 创建一个用例收集器
# 集成用例，把所有写好的测试用例收集起来

import unittest
from Lesson_python.python_unittest.test_math import test_mathTest

suite = unittest.TestSuite()    #用例收集，创建实例
suite.addTest(test_mathTest("test_add_two_positive")) # 创造测试类的实例，它是专门收集测试类的实例


