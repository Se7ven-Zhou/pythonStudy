#coding:utf-8

from selenium import webdriver

class Login_check:

    def __init__(self,driver):

        self.driver = driver

    def Login_pass(self):

        get_nickname_xpath = '//a[@class="user-name"]/span'
        get_nickname = self.driver.find_element_by_xpath(get_nickname_xpath).text
        return get_nickname
