#coding:utf-8

import win32gui
import win32con

"""
现状spy++ 和 pywin32三方库,
"""

dialog = win32gui.FindWindow("#32770","打开") #（class ,Title ）

ComboBoxEx32 = win32gui.FindWindow(dialog,0,"ComboBoxEx32",None)

button = win32gui.FindWindow(dialog,0,"Button","打开($0)") #(上一层名称，0(查找全部子窗口)，class，Text)

file_path = "D:\\111.txt"

#操作
win32gui.SendMessage(edit,win32con.WM_SETTEXT,None,file_path)
win32gui.SendMessage(dialog,win32con.WM_COMMAND,1,button)