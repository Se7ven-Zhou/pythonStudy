# coding:utf-8

from appium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import By
from selenium.webdriver.support.wait import WebDriverWait
from HomeWork.Appium_Video.Common.logger import Logging
import HomeWork.Appium_Video.Config.device_info

class Base_function:

    def __init__(self,driver):

        self.driver = driver
    # 等待元素可见
    def Wait_element_visible(self,by=By.ID,locator=None,wait_times=10):
        try:
            # 确定传值在键值对里
            if by not in By.__dict__.values():
                print("传入定位方式有误")
            else:
                WebDriverWait(self.driver,wait_times,5).until(EC.visibility_of_element_located((by,locator)))
        except Exception as error:
            Logging().Error(error)

    # 等待元素可见后，获取该元素
    def Find_element(self,by=By.ID,locator=None,wait_times=40):
        try:
            self.Wait_element_visible(by,locator,wait_times)
            element = self.driver.find_element(by,locator)
            return element
        except Exception as error:
            Logging().Error(error)
            Logging().Error("找不到元素定位："+ locator)

if __name__ == "__main__":
    caps  = HomeWork.Appium_Video.Config.device_info.desired_caps
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",caps)
    Base_function(driver).Find_element(locator="com.xiaomi.shop.plugin.homepage:id/main_bottom_tab_mine_icon").click()
