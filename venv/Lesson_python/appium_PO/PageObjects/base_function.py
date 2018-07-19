# coding:utf-8

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy

from selenium.webdriver.support.wait import WebDriverWait
from HomeWork.Web_PO_unittest.Logs.mylogger import Logging

class Base_function:

    def __init__(self,driver):

        self.driver = driver
    # 等待元素可见
def Wait_element_visible(self,by=By.XPATH,locator=None,wait_times=10):
        try:
            # 确定传值在键值对里
            if by not in By.__dict__.values() or by not in MobileBy.__dict__.values():
                print("传入定位方式有误")
            else:
                WebDriverWait(self.driver,wait_times,1).until(EC.visibility_of_element_located((by,locator)))
        except Exception as error:
            print(error)
            Logging().My_logger(error)

    # 等待元素可见后，获取该元素
    def Find_element(self,by=By.XPATH,locator=None,wait_times=40):
        self.Wait_element_visible(by,locator,wait_times)
        element = self.driver.find_element(by,locator)
        return element

    # 获取当前页面URL
    def get_url(self):
        return self.driver.currrent_url

    # 滚动到可见区域
    def scroll_intoView(self,ele):
        self.driver.execute_script("arguments[0].scrollIntoView():",ele)

if __name__ == "__main__":

    driver = webdriver.Firefox()
    driver.get("https://www.mi.com")

    login_link_xpath = '//a[text()="登录"]'

    # login_link = Base_function(driver).Find_element(By.XPATH,login_link_xpath)
    Base_function(driver).Wait_element_visible(By.XPATH,login_link_xpath)
    driver.find_element_by_xpath(login_link_xpath).click()