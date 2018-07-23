# coding:utf-8

import time
from appium import webdriver
from HomeWork.Appium_Video.Common.base_function import Base_function
import HomeWork.Appium_Video.Config.device_info
import HomeWork.Appium_Video.Config.account_info
from HomeWork.Appium_Video.Common.logger import Logging

class Login_page:

    # 我的按钮
    my_page_id = "com.xiaomi.shop.plugin.homepage:id/main_bottom_tab_mine_icon"
    # 点击头像登录
    image_login = "com.xiaomi.shop.plugin.homepage:id/usercentral_listheader_imageview"
    # 账号密码登录
    account_login_button_id = "com.xiaomi.shop:id/entry_to_password_login"
    # 账号输入框
    mobile_input_id = "com.xiaomi.shop:id/et_account_name"
    # 密码输入框
    password_input_id = "com.xiaomi.shop:id/et_account_password"
    # 登录按钮
    login_button_id = "com.xiaomi.shop:id/btn_login"
    # 登录用户名
    username_id = "com.xiaomi.shop.plugin.homepage:id/usercentral_listheader_username"
    # 用户名密码不匹配
    login_wrong_id = "com.xiaomi.shop:id/error_password_tips"

    def __init__(self,driver):

        self.driver = driver

    def login_function(self,mobile=HomeWork.Appium_Video.Config.account_info.mobile,password=HomeWork.Appium_Video.Config.account_info.password):
        # mobile = HomeWork.Appium_Video.Config.account_info.mobile
        # password = HomeWork.Appium_Video.Config.account_info.password
        time.sleep(5)
        Base_function(self.driver).Find_element(locator=self.my_page_id).click()
        time.sleep(3)
        Base_function(self.driver).Find_element(locator=self.image_login).click()
        time.sleep(3)
        Base_function(self.driver).Find_element(locator=self.account_login_button_id).click()
        Base_function(self.driver).Find_element(locator=self.mobile_input_id).send_keys(mobile)
        Base_function(self.driver).Find_element(locator=self.password_input_id).send_keys(password)
        Base_function(self.driver).Find_element(locator=self.login_button_id).click()


if __name__ == "__main__":
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",HomeWork.Appium_Video.Config.device_info.desired_caps)
    Login_page(driver).login_function()

