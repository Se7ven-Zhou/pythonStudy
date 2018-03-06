# coding:utf-8

import unittest     # 导入unittest框架
from Lesson_python.python_unittest.math import mathTest    # 导入测试目标类


#   写测试类，专门来测试目标类的类
class test_mathTest(unittest.TestCase):

    def setUp(self):    # 开始
        print("测试开始啦")

    def test_add_two_positive(self):    # 必须用test开头
        result = mathTest(2,3)
        print(result.add())

    def test_add_two_nagetive(self):    # 必须用test开头
        result = mathTest(-2)
        print(result.add())

    def tearDown(self):     # 结束
        print("测试结束啦")

# 写测试代码，看是否可以运行
if __name__ =="__main__":
    unittest.main()





