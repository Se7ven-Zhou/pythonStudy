# coding:utf-8

import unittest
from HomeWork.Requests_unittest.HttpRequests import httpRequests
import requests


class Test_HttpRequests(unittest.TestCase):
    def setUp(self):
        print("测试开始")

    def test_get_normal(self):
        test = httpRequests("13752852018","123456")
        result = test.Get()
        self.assertEqual("10001",result["code"],"注册失败啦！")  # self后可直接调用
        print()

    def test_get_abnormal(self):
        test = httpRequests("","123456")
        print(test.Get())

    def tearDown(self):
        print("测试结束")


if __name__ == "__main__":
    unittest.main()