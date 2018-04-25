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

""" # 滑动
target = driver.find_element_by_class_name("footer-service")
driver.execute_script("arguments[0].scrollIntoView();", target)
屏幕最底部:
js = "varq=document.documentElement.scrollTop=10000"
driver.execute_script(js)
"""
"""切换iframe

"""

class Login_test():

    def Login(self,https):
        driver = webdriver.Firefox()
        driver.get(https)

        driver.find_element_by_xpath("//a[@id='js_login']").click()
        # driver.find_element_by_link_text("登录").click()
        # driver.maximize_window()
        time.sleep(2)

        driver.find_element_by_xpath("//a[@class='js-btns-enter btns-enter btns-enter-qq']").click()
        driver.switch_to.frame("login_frame_qq")

        # driver.find_element_by_xpath("//a[@id='switcher_plogin']").click()
        # driver.find_element_by_id("u").send_keys("13752852018")
        # driver.find_element_by_id("p").send_keys("701777@xmzj")
        # driver.find_element_by_id("login_button").click()

        time.sleep(5)
        driver.close()

if __name__ == "__main__":

    Login_test().Login("https://ke.qq.com/")


# //span[text()=" lr_test"]/ancestor::a/following-sibling::div//a



