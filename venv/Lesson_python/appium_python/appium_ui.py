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
