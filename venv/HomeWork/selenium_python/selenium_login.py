# coding:utf-8

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Selenium_login:

    def login_Ke(self,https):

        driver = webdriver.Firefox()
        driver.get(https)

        driver.implicitly_wait(10)
        driver.find_element_by_id("js_login").click()
        driver.find_element_by_xpath("//a[@class='js-btns-enter btns-enter btns-enter-qq']").click()

        # 等待登录iframe出现后,再切换iframe
        iframe_login_name = "login_frame_qq"
        WebDriverWait(driver,10,1).until(EC.visibility_of_element_located((By.NAME,iframe_login_name)))
        driver.switch_to.frame(iframe_login_name)
        # 这个函数一步到位
        # WebDriverWait(driver,10,1).until(EC.frame_to_be_available_and_switch_to_it(iframe_login_name))

        # 滑动到该元素
        # ele = driver.execute_script("arguments[0].scrollIntoView();",元素)

        driver.find_element_by_id("switcher_plogin").click()
        driver.find_element_by_id("u").send_keys("406574570")
        driver.find_element_by_id("p").send_keys("xmzj@701777")
        driver.find_element_by_id("login_button").click()

if __name__ == "__main__":

    Selenium_login().login_Ke("https://ke.qq.com")


