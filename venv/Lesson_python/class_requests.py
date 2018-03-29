# coding:utf-8

import requests
import time
from openpyxl import load_workbook
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
        response = requests.get(self.url,self.params)
        return response.json()

     def Post(self):
        response = requests.post(self.url,self.params)
        return response.json()

if __name__ == "__main__":

    # url = "http://119.23.241.154:8080/futureloan/mvc/api/member/login"
    # params = {"mobilephone":"13752852018","pwd":"123456"}
    # tester = HttpRrequsts(url,params)
    # test = tester.Get()
    # print(test)

    url = "http://119.23.132.26:8091/u/login"
    params = {"params":"{'mobile':'13752852011','password':'123456','systemName':'IOS'}","signature":"82601564dc52a8e456f7c82272ba3d09","timestamp":1522305160,"admin":"!QS#$^Tghi0"}
    tester = HttpRrequsts(url,params)
    test = tester.Post()
    print(test)

# class Get_data:
#     def __init__(self,systemName="IOS",timestamp=1522305160,signature="82601564dc52a8e456f7c82272ba3d09",admin="!QS#$^Tghi0"):
#         self.systemName = systemName
#         self.timestamp =timestamp
#         self.signature = signature
#         self.admin = admin
#
#     def Read_excel(self,path):
#         file = load_workbook(path)
#         sheet = file.get_sheet_by_name("python_test")
#         test_data_list = []
#
#         for item in range(2, sheet.max_row + 1):
#             data_params = {}
#             params = {}
#             data_params["mobile"] = sheet.cell(row=item, column=1).value
#             data_params["password"] = sheet.cell(row=item, column=2).value
#             data_params["systemName"] = self.systemName
#
#             params["params"] = data_params
#             params["timestamp"] = self.timestamp
#             params["signature"] = self.signature
#             params["admin"] = self.admin
#             file.save(path)
#             print(params)
#
# if __name__ == "__main__":
#
#     data_params = Get_data().Read_excel("test.xlsx")
#     print(data_params)