# coding:utf-8

from appium import webdriver

# 设备信息
desired_caps = {}
desired_caps["deviceName"] = "Android Emulator"
desired_caps["platformName"] = "Android"
desired_caps["platformVersion"] = "4.4.2"
desired_caps["appPackage"] = "com.hushi.video"
desired_caps["appActivity"] = ".activity.MainActivity"


driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
driver.implicitly_wait(30) # 等待

ele = driver.find_element_by_id("")
size = ele.size

from appium.webdriver.common.touch_action import TouchAction