#coding:utf-8

from selenium import webdriver
from HomeWork.WebAuto_selenium.PageObjects.function_login import Function_login
from HomeWork.WebAuto_selenium.PageObjects.login_check import Login_check
import time

# 登录
driver = webdriver.Firefox()
mobile = "13752852018"
password = "701777xmzj"
Function_login(driver).Login(mobile,password)

time.sleep(3)

# 验证登录成功
lc = Login_check(driver).Login_pass("Aslin")






