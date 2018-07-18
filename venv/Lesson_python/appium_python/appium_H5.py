# coding:utf-8

from appium import webdriver

# 设备信息
desired_caps = {}
desired_caps["deviceName"] = "Android Emulator"
desired_caps["platformName"] = "Android"
desired_caps["platformVersion"] = "4.4.2"
desired_caps["appPackage"] = "com.hushi.video"
desired_caps["appActivity"] = ".activity.MainActivity"

"""
Genymotion用不起的
https://blog.csdn.net/scythe666/article/details/70216144
"""


driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
driver.implicitly_wait(20)
# Uiautonator定位元素，注意文本内容只能是双引号
driver.find_element_by_android_uiautomator('new UiSelector().text("全程班")')

# 获取上下文
contexts = driver.contexts
# 开启Webview权限
"""Tips : setWebContentDebuggingEnable(true) # 需要开发开启这个权限"""

# 切换
driver.switch_to.context("") # 这个要切换到的参数来自contexts的web名称，可以先打印出来看看
# Chrome://inspect/#devices  进入H5页面后，打开谷歌浏览器输入

# web端操作:chromedriver.exe一定要匹配Android手机系统自带的内核chrome版本
driver.find_element_by_id("").click()

# 返回原生页
driver.switch_to.content(None)