# coding:utf-8

import unittest
from HomeWork.unittest_0314_excel.http_requests import Http_requests

class test_Http_requests(unittest.TestCase):
    def __init__(self,methodName,url,params):
        super(test_Http_requests, self).__init__(methodName)
        self.url=url
        self.params = params

    def setUp(self):
        print("测试开始")

    def test_register_excel(self):
        test = Http_requests(self.url,self.params).Get()
        print(test)

    def tearDown(self):
        print("测试结束")


if __name__ == "__main__":
    unittest.main()