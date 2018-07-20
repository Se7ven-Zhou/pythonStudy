# coding:utf-8

from appium import webdriver

# 设备信息
desired_caps = {}
desired_caps["deviceName"] = "Android Emulator"
desired_caps["platformName"] = "Android"
desired_caps["platformVersion"] = "4.4.2"
desired_caps["appPackage"] = "com.hushi.video"
desired_caps["appActivity"] = ".activity.MainActivity"
desired_caps["noReset"] = True


driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
driver.implicitly_wait(30) # 等待

# ele = driver.find_element_by_id("")
# size = ele.size
#
# from appium.webdriver.common.touch_action import TouchAction
#
# ta = TouchAction(driver) # TouchAction需要初始化一个driver驱动，实例化
# # 实例化后就可以操作，这些方法返回参数都是实例，所以可以很多操作连续做，最后释放再执行
# ta.press(x="",y="").wait(200).move_to(x="",y="").wait(200).move_to(x="",y="").release().perform()

"""安装、卸载、启动、关闭"""
# # 启动 Activity
# driver.start_activity("包名")
# # 安装应用, / 是否安装
# driver.install_app("path/to/my.apk")
# driver.is_app_installed("包名")
# # 卸载应用
# driver.remove_app("包名")
# # 关闭应用
# driver.close_app()

"""拉取、推送文件"""
# driver.pull_file("Library/AddressBook/AddressBook.sqlitdb")
# data = "some data for the file"
# path = "/data/local/tmp/file.txt"
# driver.push_file(path,data.encode("base64"))

"""唤醒"""
# driver.lock(5) # 锁定5秒，适用ios，安卓不能唤醒
# driver.background_app({"timeout":secs}) # 如果timeout = -1 or null，则表示持续置于后台

"""打开通知栏、摇一摇"""
# driver.open_notification() # 仅支持安卓
# driver.shake()

"""放大、缩小"""
# driver.pinch(element = el)
# dirver.zoom(element =el)

"""隐藏键盘"""
# driver.hide_keyboard() # 隐藏键盘

"""按键操作"""
# driver.press_keycode(键值)
# KEYCODE_CALL  拨号键       5
# KEYCODE_ENDCALL 挂机键     6
# KEYCODE_HOME HOME键        3
# KEYCODE_MENU    菜单键     82
# KEYCODE_SEARCH  搜索键     84
# KEYCODE_BACK    返回键     4
# KEYCODE_CAMERA  拍照键     27
# KEYCODE_FOCUS   拍照对焦键 80
# KEYCODE_POWER   电源键     26
# KEYCODE_NOTIFICATION 通知键 83
# KEYCODE_MUTE    静音键     91
# KEYCODE_VOLUME_MUTE 话筒静音键 164
# KEYCODE_VOLUME_UP 音量增加键 24
# KEYCODE_VOLUME_DOWN 音量减小键 25
# https://blog.csdn.net/crisschan/article/details/50419963#t1  详细描述更多

