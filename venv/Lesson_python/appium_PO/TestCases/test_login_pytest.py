#coding:utf-8

from selenium import webdriver
from HomeWork.Web_PO_unittest.PageObjects.login_page import Login_page
from HomeWork.Web_PO_unittest.PageObjects.index_page import Index_page
from HomeWork.Web_PO_unittest.TestDatas import read_datas
from HomeWork.Web_PO_unittest.TestDatas import CommonData
import time
import unittest
import pytest

"""
调用fixture三种方法
1.fixture的函数名，传递给测试用例
"""

# @pytest.mark.usefixture("init_env")
# class Test_login():
#
#     @pytest.fixture
#     def init_driver(self):
#
#         self.driver = webdriver.Firefox()
#         self.driver.implicitly_wait(10)
#         yield
#         self.driver.quit()
#
#     @pytest.mark.smoke
#     def test_login_success(self,init_driver):
#         # 测试数据
#         mobile = "13752852018"
#         password = "701777xmzj"
#         username = "Se7ven"
#
#         # 步骤
#         Login_page(self.driver, CommonData.url).Login_function(mobile,password)
#         nickname = Index_page(self.driver).Login_name()
#         # 检验
#         assert nickname == username

    # def test_login_fail(self):
    #     # 测试数据
    #     mobile = "13752852018"
    #     password = "123456abc"
    #     wrong_msg = "用户名或密码不正确"
    #     # 步骤
    #     Login_page(self.driver, self.url).Login_function(mobile, password)
    #     get_wrong_msg = Index_page(self.driver).Login_fail_msg()
    #     # 检验
    #     self.assertEqual(get_wrong_msg,wrong_msg)

if __name__ == "__main__":

    pytest.main(["-m","smoke"])
