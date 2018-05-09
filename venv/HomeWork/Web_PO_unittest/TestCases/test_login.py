#coding:utf-8

from selenium import webdriver
from HomeWork.Web_PO_unittest.PageObjects.login_page import Login_page
from HomeWork.Web_PO_unittest.PageObjects.index_page import Index_page
from HomeWork.Web_PO_unittest.TestDatas import read_datas
import time
import unittest

class Login_test(unittest.TestCase):

    def __init__(self,methodName,user_info):
        super(Login_test, self).__init__(methodName)
        self.user_info = user_info

    def setUp(self):

        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.url = "https://www.mi.com/"

    def test_login_success(self):
        # 测试数据
        mobile = self.user_info["mobile"]
        password = self.user_info["password"]
        username = self.user_info["nickname"]

        # 步骤
        Login_page(self.driver,self.url).Login_function(mobile,password)
        nickname = Index_page(self.driver).Login_name()
        # 检验
        self.assertEqual(nickname, username)

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

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":

    unittest.main()