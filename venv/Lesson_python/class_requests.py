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
"""我写的"""
# class Requests:
#     def __init__(self,mobilephone,pwd):
#         self.mobile = mobilephone
#         self.password = pwd
#         self.url = url = "http://119.23.241.154:8080/futureloan/mvc/api/member/register"
#
#     def Get(self):
#         # url = "http://119.23.241.154:8080/futureloan/mvc/api/member/register"
#         params = {"mobilephone":self.mobile,"pwd":self.password}
#         response = requests.get(self.url,params)
#         return response.json()
#
#     def Post(self):
#         params = {"mobilephone":self.mobile,"pwd":self.password}
#         response = requests.get(url,params)
#         return response.json()

"""老师写的"""

class HttpRrequsts:

    def __init__(self,url,params):
        self.url = url
        self.params = params

    def Get(self):
        response = requests.get(url,params)
        return response.json()

    def Post(self):
        response = requests.post(url,params)
        return response.json()

if __name__ == "__main__":



    url = "http://119.23.241.154:8080/futureloan/mvc/api/member/register"
    params = {"mobilephone":"13752852018","pwd":"123456"}
    tester = HttpRrequsts(url,params)
    test = tester.Get()
    print(test)
