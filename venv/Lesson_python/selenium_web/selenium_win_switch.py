#coding:utf-8

from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class windows_switch:

    def win_switch(self,https):

        driver = webdriver.Firefox()
        driver.get(https)

        driver.implicitly_wait(20)
        
        driver.find_element_by_id("kw").send_keys("selenium")
        driver.find_element_by_id("su").click()

        baike_xpath = '//a[contains(text(),"百科")]'
        selenium_baike = driver.window_handles

        driver.find_element_by_xpath(baike_xpath).click()
        # 窗口出现后，进行操作
        WebDriverWait(driver,15,1).until(EC.new_window_is_opened(selenium_baike))
        # 切换窗口，获取窗口handle名称（是个列表）
        selenium_baike = driver.window_handles
        driver.switch_to.window(selenium_baike[-1])
        time.sleep(3)
        driver.find_element_by_xpath('//a[text()="功能"]').click()


if __name__ == "__main__":
    windows_switch().win_switch("https://baidu.com")