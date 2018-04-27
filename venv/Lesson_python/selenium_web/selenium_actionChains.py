#coding:utf-8

from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
"""
ActionChains.double_click()
ActionChains.context_click()
ActionChains.drag_and_drop()
ActionChains.move_by_offset()
"""

driver = webdriver.Firefox()
driver.get("https://baidu.com")

setting_xpath = '//div[@id="u1"]/a[@name="tj_settingicon"]'
setting_locator = driver.find_element_by_xpath(setting_xpath)
# 先实例，再动作，再执行
ActionChains(driver).move_to_element(setting_locator).perform()  # 参数to_element 是元素实例不是locato#

# 遍历下拉菜单的Xpath 鼠标挨着放上去
for item in range(1,5):
    detail_xpath = str([item])
    locator_xpath = '//div[@class="bdnuarrow"]/following-sibling::a'
    final_xpath = locator_xpath + detail_xpath
    element_locator = driver.find_element_by_xpath(final_xpath)
    ActionChains(driver).move_to_element(element_locator).perform()