# coding:utf-8

import unittest
from HomeWork.unittest_0313.http_requests import httpRequests
from HomeWork.unittest_0313.read_data import Read_data
import requests

class Test_HttpRequests(unittest.TestCase):

    def __init__(self,methodName,mobile,pwd):
        super(Test_HttpRequests, self).__init__(methodName)     # 超继承
        self.mobile = mobile
        self.pwd = pwd

    def setUp(self):
        print("测试开始")

    def test_register(self):
        test = httpRequests(self.mobile,self.pwd).Get()
        return test

    def tearDown(self):
        print("测试结束")

if __name__ == "__main__":
    unittest.main()