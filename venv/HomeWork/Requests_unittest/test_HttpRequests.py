# coding:utf-8

import unittest
from HomeWork.Requests_unittest.HttpRequests import httpRequests
from HomeWork.Requests_unittest.HttpRequests import Read_data
import requests


class Test_HttpRequests(unittest.TestCase,Read_data):
    def setUp(self):
        print("测试开始")

    def test_get_normal(self):

        """方法一：用例里遍历参数"""
        data = Read_data()
        data_in = data.read_data("test.txt")

        for item in range(0,len(data_in)):
            # print(data_in[item]["mobilephone"])
            test = httpRequests(data_in[item]["mobilephone"],data_in[item]["pwd"])
            print(test.Get())

        # data = Read_data()
        # data_in = data.read_data("test.txt")
        # test = httpRequests(data_in[item]["mobilephone"],data_in[item]["pwd"])
        # result = test.Get()
        # # self.assertEqual("10001",result["code"],"注册失败啦！")  # self后可直接调用
        # print(result)

    # def test_get_abnormal(self):
    #     test = httpRequests("15123645350","123456")
    #     print(test.Get())

    def tearDown(self):
        print("测试结束")


if __name__ == "__main__":
    unittest.main()