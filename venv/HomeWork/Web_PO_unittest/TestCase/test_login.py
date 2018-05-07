#coding:utf-8

from selenium import webdriver
from HomeWork.Web_PO_unittest.PageObject.login_page import Login_page
from HomeWork.Web_PO_unittest.PageObject.index_page import Index_page
import time
import unittest

class Login_test(unittest.TestCase):

    def setUp(self):
        self.url = "https://www.mi.com/"


    def test_login_success(self,mobile,password,username):
        driver = webdriver.Firefox()
        # 步骤
        Login_page(driver,self.url).Login_function(mobile,password)
        nickname = Index_page(driver).Login_name()
        # 检验
        self.assertEqual(nickname, username)

    def test_login_fail(self):
        pass

    # def tearDown(self):
    #     driver.quit()

if __name__ == "__main__":
    Login_test().test_login_success("13752852018","701777xmzj","Se7ven")