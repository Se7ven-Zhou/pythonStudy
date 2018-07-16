# coding:utf-8

"""
TextView 文本框
EditView 编辑框
Button 按钮
RadioButton 单选按钮
CheckBox 复选框
ToggleButton 状态开关按钮
Switch 开关
SeekBar 拖动条
"""
# adb shell dumpsys activity | findstr "mFocusedActivity" 查看启动和包名

from appium import webdriver

# 设备信息
desired_caps = {}
desired_caps["deviceName"] = "Android Emulator"
desired_caps["platformName"] = "Android"
desired_caps["platformVersion"] = "4.4.2"
desired_caps["appPackage"] = "com.hushi.video"
desired_caps["appWaitActivity"] = ".activity.MainActivity"

# 链接appium server
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)

# resource-id
driver.find_element_by_id("")
#content-desc
driver.find_element_by_accessibility_id("")
# uiautonator
driver.find_element_by_android_uiautomator("new UiSelector().resourceid('')")
driver.find_element_by_android_uiautomator("new UiSelector().textContains('')")
# 百度查看“UiSelector”的很多函数方法
# text
# text("")
# textContains("")
# textStartWith("") 以什么开头

# 滑动屏幕
device_size = driver.get_window_size()
# 其实位置
start_x = device_size["width"] * 0.9
start_y = device_size["height"] * 0.5
# 终点位置
end_x = device_size["width"] * 0.1
end_y = device_size["height"] * 0.5

driver.swipe(start_x,start_y,end_x,end_y)

"""TouchActionl类"""
# press
# longpress
# tap
# move_to
# wait
# release
# perform
# cancel
