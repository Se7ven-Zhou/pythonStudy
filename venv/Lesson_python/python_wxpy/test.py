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

import tkinter

root = tkinter.Tk()
root.title("Python tkinter")

labelIP = tkinter.Label(root,text="服务器地址：").grid(row=1,column=1)
textIP = tkinter.Entry(root).grid(row=1,column=2)
labelPort = tkinter.Label(root,text="端口：").grid(row=1,column=3)
textPort = tkinter.Entry(root).grid(row=1,column=4)

labelAPI = tkinter.Label(root,text="接口地址：").grid(row=2,column=1)
textAPI = tkinter.Entry(root).grid(row=2,column=2)
btnRun = tkinter.Button(root,text="Run",fg="red").grid(row=2,column=3)

textRequest = tkinter.Text().grid(row=3,column=1)
textResponse = tkinter.Text().grid(row=3,column=2)

root.mainloop()


