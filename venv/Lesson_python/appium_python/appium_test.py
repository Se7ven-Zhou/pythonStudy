# coding:utf-8

import time
from appium import webdriver

# 设备信息
desired_caps = {}
desired_caps["deviceName"] = "Android Emulator"
desired_caps["platformName"] = "Android"
desired_caps["platformVersion"] = "4.4.2"
desired_caps["appPackage"] = "com.hushi.video"
desired_caps["appActivity"] = ".activity.MainActivity"
# desired_caps["appPackage"] = "com.xiaomi.shop"
# desired_caps["appActivity"] = "com.xiaomi.shop2.activity.MainActivity"
desired_caps["noReset"] = True

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
driver.implicitly_wait(5) # 等待

driver.find_element_by_id("com.hushi.video:id/title_end_img").click()
time.sleep(3)
driver.find_element_by_class_name("android.widget.EditText").send_keys("zj")
# driver.find_element_by_id("com.hushi.video:id/title_edit").send_keys("123")
#driver.find_element_by_android_uiautomator("new UiSelector().textContains('_IMG_  请输入关键字')").send_keys("zj")
time.sleep(3)
driver.find_element_by_id("com.hushi.video:id/title_search").click()

# driver.find_element_by_android_uiautomator("new UiSelector().resourceid('com.hushi.video:id/title_end_img')").click()
# driver.find_element_by_android_uiautomator("new UiSelector().resourceid('com.hushi.video:id/title_edit')").send_keys("zj")
# driver.find_element_by_android_uiautomator("new UiSelector().resourceid('com.hushi.video:id/title_search')").click()

# driver.find_element_by_id("com.xiaomi.shop.plugin.homepage:id/fragment_search_swither").send_keys("123")