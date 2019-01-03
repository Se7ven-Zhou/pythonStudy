# coding:utf-8

# from tkinter import *
#
# root = Tk()
# root.title('Python Tkinter')
#
# str = """At present, only GIF and PPM/PGM
# formats are supported, but an interface
# exists to allow additional image file
# formats to be added easily."""
# logo = PhotoImage(file="G:/1.gif")
# lb = Label(root,text=str,image=logo,compound = LEFT).pack(side = LEFT)


# import tkinter as tk
# import time
# counter = 0
#
# # 计时器
# def counter_label(label):
#     def count():
#         global counter
#         counter += 1
#         label.config(text=str(counter))
#         label.after(1000, count)
#     count()
#
#
# root = tk.Tk()
# root.title("Counting Seconds")
# label = tk.Label(root, fg="green")
# label.pack()
# counter_label(label)
# button = tk.Button(root, text='Stop', width=25, command=root.destroy)
# button.pack()
# root.mainloop()

# import tkinter
#
# root = tkinter.Tk()
# root.title("Python tkinter")
#
# labelIP = tkinter.Label(root,text="服务器地址：").grid(row=1,column=1)
# textIP = tkinter.Entry(root).grid(row=1,column=2)
# labelPort = tkinter.Label(root,text="端口：").grid(row=1,column=3)
# textPort = tkinter.Entry(root).grid(row=1,column=4)
#
# labelAPI = tkinter.Label(root,text="接口地址：").grid(row=2,column=1)
# textAPI = tkinter.Entry(root).grid(row=2,column=2)
# btnRun = tkinter.Button(root,text="Run",fg="red").grid(row=2,column=3)
#
# textRequest = tkinter.Text().grid(row=3,column=1)
# textResponse = tkinter.Text().grid(row=3,column=2)
#
# root.mainloop()

"""
<modifier->---type-<-detail>
键位对应名称：https://infohost.nmt.edu/tcc/help/pubs/tkinter/web/key-names.html
"""
"""点击出效果"""
# import  tkinter
#
# def presslabel(envent):
#     global baseframe
#     tkinter.Label(baseframe,text="欢迎点击").pack()
#
# baseframe = tkinter.Tk()
# lb = tkinter.Button(baseframe,text="点击试试")
# lb.bind("<Button-1>",presslabel)
# lb.pack()
#
# baseframe.mainloop()
"""登录"""
# import tkinter
#
# def login():
#     us = username.get()
#     pw = pwd.get()
#     t1 = len(us)
#     t2 = len(pw)
#
#     if us == "zj" and pw == "abc":
#         marked["text"] = "登录成功"
#     else:
#         marked["text"] = "用户名或密码错误"
#         username.delete(0,t1)
#         pwd.delete(0,t2)
#
# baseFrame = tkinter.Tk()
#
# tkinter.Label(baseFrame,text="用户名").grid(row=0,column=0)
# username = tkinter.Entry(baseFrame)
# username.grid(row=0,column=1)
#
# tkinter.Label(baseFrame,text="密码").grid(row=1,column=0)
# pwd = tkinter.Entry(baseFrame)
# pwd.grid(row=1,column=1)
# pwd["show"] = "*"
#
# tkinter.Button(baseFrame,text="登录",command=login).grid(row=2,column=1)
# marked = tkinter.Label(baseFrame,text="")
# marked.grid(row=3,column=0)
#
# baseFrame.mainloop()

"""
菜单：
1.普通菜单：
    第一个menu类定义的是parent
    add_command 添加菜单项，如果是顶层菜单，则从左向右添加，否则就是下拉菜单
    label：指定菜单项名称
    command：点击后相应的调用函数
    acceletor：快捷键
    underline：制定是否菜单信息有下划线
    menu：属性制定使用哪一个作为顶级菜单
"""
"""普通/集联菜单"""
# import tkinter
# #
# # baseFrame = tkinter.Tk()
# # menubar = tkinter.Menu(baseFrame)
# # menuSon = tkinter.Menu(menubar)
# #
# # for item in ["aaa","bbb","ccc","ddd"]:
# #     menuSon.add_command(label=item)
# #
# # menubar.add_cascade(label="File")
# # menubar.add_cascade(label="Edit",menu=menuSon)
# # menubar.add_cascade(label="help")
# #
# # baseFrame["menu"] = menubar
# # baseFrame.mainloop()
"""弹出式菜单"""
# import tkinter
#
# baseFrame = tkinter.Tk()
# menubar = tkinter.Menu(baseFrame)
#
# def marked():
#     global baseFrame
#     tkinter.Label(baseFrame,text="预定成功").pack()
#
# for item in ["aaa","bbb","ccc"]:
#     menubar.add_separator()
#     menubar.add_command(label=item)
#
# menubar.add_command(label="ddd",command=marked)
#
# def pop(event):
#     menubar.post(event.x_root,event.y_root)
#
# baseFrame.bind("<Button-3>",pop)
# baseFrame.mainloop()
"""画布：画五角星"""
import tkinter,math

baseFrame = tkinter.Tk()
# p = tkinter.Canvas(baseFrame,width=300,height=300,)
# p.pack()
#
# center_x = 150
# center_y = 150
#
# point_1_x = int(center_x)
# point_1_y = int(center_y) + 100
#
# point_2_x = int(center_x) + 100
# point_2_y = int(center_y)
#
# point_3_x = int(center_x) + 50
# point_3_y = int(center_y) - 100
#
# point_4_x = int(center_x) - 50
# point_4_y = int(center_y) - 100
#
# point_5_x = int(center_x) - 100
# point_5_y = int(center_y)
#
# p.create_line(point_1_x,point_1_y, point_3_x,point_3_y)
# p.create_line(point_1_x,point_1_y, point_4_x,point_4_y)
#
# p.create_line(point_2_x,point_2_y, point_4_x,point_4_y)
# p.create_line(point_2_x,point_2_y, point_5_x,point_5_y)
#
# p.create_line(point_3_x,point_3_y, point_5_x,point_5_y)
#
# baseFrame.mainloop()
# # 创建一个多边形
# p.create_polygon(points,outline="",fill="")
# 移动
w = tkinter.Canvas(baseFrame,width=500,height=500)
w.pack()
id_ball = w.create_oval(20,20, 50,50, fill="green")
w.move(id_ball, 12,5)
