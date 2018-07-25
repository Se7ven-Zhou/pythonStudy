# coding:utf-8

from appium import webdriver
from HomeWork.Appium_Video.Config import device_info

class Base_Driver:

    def __init__(self):

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",device_info.desired_caps)
        self.driver.implicitly_wait(10)