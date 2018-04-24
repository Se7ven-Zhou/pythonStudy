# coding:utf-8

import time
from selenium import webdriver

"""
Xpath定位语法
<input class="item_account" autocomplete="off" type="text" name="user" id="username" placeholder="邮箱/手机号码/小米ID">
//标签[@属性=值]
//input[@id="username"]

ancestor    祖先结点
parent      父节点
preceding   当前元素结点标签之前的所有结点
preceding-sibling   当前元素结点标签之前的所有兄弟结点
following   当前元素标签之后的所有结点
following-sibling   当前元素标签之后的所有兄弟结点      

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


# //span[text()=" lr_test"]/ancestor::a/following-sibling::div//a
