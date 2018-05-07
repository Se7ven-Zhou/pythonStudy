# coding : utf-8

from selenium import webdriver

class Index_page:

    # 首页xpath定位
    get_nickname_xpath = '//a[@class="user-name"]/span'

    def __init__(self,driver):
        self.driver = driver

    def Login_name(self):

        get_nickname = self.driver.find_element_by_xpath(self.get_nickname_xpath).text
        return get_nickname

    def No_username_msg(self):
        pass

    def No_password_msg(self):
        pass

    def Login_fail_msg(self):
        pass
