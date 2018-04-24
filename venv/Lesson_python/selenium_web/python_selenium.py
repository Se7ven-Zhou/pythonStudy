# coding:utf-8

import time
from selenium import webdriver

"""
Xpath定位语法
<input class="item_account" autocomplete="off" type="text" name="user" id="username" placeholder="邮箱/手机号码/小米ID">
//标签[@属性=值]
//input[@id="username"]
"""

class Login_test():

    def Login_xiaomi(self,https):
        driver = webdriver.Firefox()
        driver.get(https)

        driver.find_element_by_link_text("登录").click()
        driver.maximize_window()

        time.sleep(2)
        driver.find_element_by_id("username").send_keys("13752852018")
        driver.find_element_by_id("pwd").send_keys("701777xmzj")
        driver.find_element_by_id("login-button").click()
        driver.close()

if __name__ == "__main__":

    Login_test().Login_xiaomi("https://www.mi.com/")



