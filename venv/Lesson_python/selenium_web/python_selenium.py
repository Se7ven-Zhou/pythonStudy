# coding:utf-8

import time
from selenium import webdriver

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

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

"""
强制等待：   time.sleep()
隐形等待：   implicitly_wait()
显性等待：明确等待某个条件满足了就执行下一步，设置最长时间，抛出TimeoutException

"""

class Login_test():

    # def Login(self,https):
    #     driver = webdriver.Firefox()
    #     driver.get(https)
    #     driver.implicitly_wait(30)  # 最长等待30秒，智能等待
    #
    #     driver.find_element_by_xpath("//a[@id='js_login']").click()
    #     driver.find_element_by_link_text("登录").click()
    #     # driver.maximize_window()
    #     time.sleep(2)
    #
    #     driver.find_element_by_xpath("//a[@class='js-btns-enter btns-enter btns-enter-qq']").click()
    #     driver.switch_to.frame("login_frame_qq")
    #     time.sleep(3)
    #     driver.find_element_by_id("switcher_plogin").click()
    #     driver.find_element_by_id("u").send_keys("13752852018")
    #     driver.find_element_by_id("p").send_keys("701777@xmzj")
    #     driver.find_element_by_id("login_button").click()
    #
    #     time.sleep(5)
    #     # driver.close()  # 关闭浏览器
    #     driver.quit()   # 关闭浏览器并退出ChromeDriver

    def Login_baidu(self,https):
        driver = webdriver.Firefox()
        driver.get(https)

        driver.find_element_by_xpath("//div[@id='u1']/a[@name='tj_login']").click()

        # 判断特定条件出现后再执行下一步操作，确定弹出框出现再操作
        login_pop_id = "//p[@class='tang-pass-footerBarULogin pass-link']"
        WebDriverWait(driver,10,1).until(EC.visibility_of_element_located((By.XPATH,login_pop_id)))
        driver.find_element_by_xpath(login_pop_id).click()

if __name__ == "__main__":

    Login_test().Login_baidu("https://baidu.com")


# //span[text()=" lr_test"]/ancestor::a/following-sibling::div//a



