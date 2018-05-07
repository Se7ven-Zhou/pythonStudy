#coding:utf-8

from selenium import webdriver

class Function_login:

    url = "https://www.mi.com/"
    login_click_xpath = '//a[text()="登录"]'
    username_xpath = '//input[@id="username"]'
    password_xpath = '//input[@name="password"]'
    button_xpath = '//input[@id="login-button"]'

    def __init__(self,driver):

        self.driver = driver
        driver.get(self.url)

    def Login(self,mobile,password):

        self.driver.find_element_by_xpath(self.login_click_xpath).click()
        self.driver.find_element_by_xpath(self.username_xpath).send_keys(mobile)
        self.driver.find_element_by_xpath(self.password_xpath).send_keys(password)
        self.driver.find_element_by_xpath(self.button_xpath).click()

