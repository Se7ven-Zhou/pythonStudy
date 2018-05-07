#coding:utf-8

from selenium import webdriver
from HomeWork.Web_PO_unittest.PageObject.login_page import Login_page
from HomeWork.Web_PO_unittest.PageObject.index_page import Index_page
import time
import unittest

class Login_test(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.url = "https://www.mi.com/"

    def test_login_success(self):
        # 测试数据
        mobile = "13752852018"
        password = "701777xmzj"
        username = "Se7ven"
        # 步骤
        Login_page(self.driver,self.url).Login_function(mobile,password)
        nickname = Index_page(self.driver).Login_name()
        # 检验
        self.assertEqual(nickname, username)

    def test_login_fail(self):
        pass

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":

    unittest.main()