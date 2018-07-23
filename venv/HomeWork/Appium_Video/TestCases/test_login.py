# coding:utf-8

from appium import webdriver
from HomeWork.Appium_Video.PageObject.login_page import Login_page
import HomeWork.Appium_Video.Config.device_info
import HomeWork.Appium_Video.Config.account_info
from HomeWork.Appium_Video.Common.base_function import Base_function
from HomeWork.Appium_Video.Common.logger import Logging
import unittest

class Test_login(unittest.TestCase):

    def setUp(self):

        pass

    def tearDown(self):

        self.driver.quit()

    def __init__(self,methodName):

        super(Test_login, self).__init__(methodName)
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",HomeWork.Appium_Video.Config.device_info.desired_caps)

    def test_login_normal(self):
        mobile = "13752852018"
        password = "701777xmzj"
        Login_page(self.driver).login_function(mobile,password)
        username = Base_function(self.driver).Find_element(locator=self.username_id).text
        assert username == "Se7ven",Logging().Error("账号不对")

    def test_login_Nopassword(self):

        mobile = "13752852018"
        password = ""
        Login_page(self.driver).login_function(mobile,password)
        error_messsage = Base_function(self.driver).Find_element(locator=Login_page.login_wrong_id).text
        assert error_messsage == "密码不能为空",Logging().Error("账号不对")

    def test_login_wrongAccount(self):

        mobile = "13752852018"
        password = "123456"
        Login_page(self.driver).login_function(mobile,password)
        error_messsage = Base_function(self.driver).Find_element(locator=Login_page.login_wrong_id).text
        assert error_messsage == "用户名密码不匹配",Logging().Error("账号不对")

if __name__ == "__main__":

    unittest.main()