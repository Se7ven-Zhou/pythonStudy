# coding:utf-8

import unittest
from HomeWork.unittest_config.http_requests import Http_requests

class test_Http_requests(unittest.TestCase):
    def __init__(self,methodName,url,params):
        super(test_Http_requests, self).__init__(methodName)
        self.url=url
        self.params = params

    def setUp(self):
        print("测试开始")

    def test_login_excel(self):
        test = Http_requests(self.url,self.params).Post()
        if test["errcode"] == "0":
            pass
        else:
            message = test["errmsg"]
            self.assertEqual("0",test["errcode"],message)   # 断言

    def tearDown(self):
        print("测试结束")


if __name__ == "__main__":
    url = "http://119.23.132.26:8091/u/login"
    params = {"params":"{'mobile':'13752852018','password':'123456','systemName':'IOS'}","signature":"82601564dc52a8e456f7c82272ba3d09","timestamp":1522305160,"admin":"!QS#$^Tghi0"}
    test = test_Http_requests("test_login_excel",url,params).test_login_excel()
    print(test)
    # unittest.main()