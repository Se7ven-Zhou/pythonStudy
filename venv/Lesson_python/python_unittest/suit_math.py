# coding:utf-8

# 创建一个用例收集器
# 集成用例，把所有写好的测试用例收集起来

import unittest
from Lesson_python.python_unittest.test_math import test_mathTest

"""收集测试用例方法一：一条一条的添加(用的方法：addtest)"""
# suite = unittest.TestSuite()    #用例收集，创建实例
# suite.addTest(test_mathTest("test_add_two_positive")) # 创造测试类的实例，它是专门收集测试类的实例
# suite.addTest(test_mathTest("test_add_two_nagetive"))

"""收集测试用例方法二：用方法：addtests ,里面是实例测试类的列表"""
# suite = unittest.TestSuite()
# suite.addTests([test_mathTest("test_add_two_positive"),test_mathTest("test_add_two_nagetive")])

"""收集测试用例方法三：从 模块名 里面去加载以test开头的
方法：创建一个加载器，然后一次性把模块名里面的用例全部加到suite里"""
from Lesson_python.python_unittest import test_math

suite = unittest.TestSuite()
loader = unittest.TestLoader()  #创建一个用例加载器实例
suite.addTest(loader.loadTestsFromModule(test_math))

"""收集测试用例方法四：用加载器加载一个类的所有用例，然后全部给suite"""
# suite = unittest.TestSuite()
# loader = unittest.TestLoader()
# suite.addTests(loader.loadTestsFromTestCase(test_mathTest))

# 执行用例，生成txt报告
# with open("test.txt","w+") as f:
#      runner = unittest.TextTestRunner(stream=f, descriptions="测试成功", verbosity=2)  # 创建一个执行用例的实例
#      runner.run(suite)   # 调用run方法执行suite用例
print(suite)
