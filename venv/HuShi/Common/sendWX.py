# coding:utf-8

from wxpy import *
import time


class SendWX:

    def __init__(self,name = "HS",groupNanme = "叽叽喳喳"):

        self.bot = Bot(cache_path=True)
        self.friend = self.bot.friends().search(name)[0]
        self.time = time.strftime('%Y-%m-%d %H:%M:%S')
        self.group = self.bot.groups().search(groupNanme)[0]

    def  System_error(self,api):
        message = "["+ self.time + "]接口:" + api + "系统异常"
        self.friend.send(message)
        self.group.send(message)

    def No_service(self,api):
        message = "["+ self.time + "]接口:" + api +  "无服务"
        self.friend.send(message)

    def Logic_error(self,api):
        message = "["+ self.time + "]接口:" + api +  "逻辑错误"
        self.friend.send(message)

if __name__ == "__main__":

    SendWX().System_error("/api/login")

