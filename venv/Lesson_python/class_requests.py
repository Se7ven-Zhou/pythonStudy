# coding:utf-8

import requests

# url = "http://119.23.241.154:8080/futureloan/mvc/api/member/register"
# params = {"mobilephone":"13100000000","pwd":"123456"}
# result = requests.post(url,params)
#
#
# print(result.encoding)      # 查看编码
# print(result.status_code)   # 查看状态码
# print(result.text)      # 查看信息
#
# content = result.json()
# print(result.json())    # 返回Json格式（字典dict类型）
#
# print(content['msg'])

class Requests:
    def __init__(self,mobilephone,pwd):
        self.mobile = mobilephone
        self.password = pwd
        self.url = url = "http://119.23.241.154:8080/futureloan/mvc/api/member/register"

    def Get(self):
        # url = "http://119.23.241.154:8080/futureloan/mvc/api/member/register"
        params = {"mobilephone":self.mobile,"pwd":self.password}
        req = requests.get(self.url,params)
        return req.json()

    def Post(self):
        params = {"mobilephone":self.mobile,"pwd":self.password}
        req = requests.get(url,params)
        return req.json()

get = Requests("13100000000","123456")
result = get.Get()
print(result)