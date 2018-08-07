# coding:utf-8

from openpyxl import Workbook
from openpyxl import load_workbook

name = ["seven","aslin","eleven","six"]

"""创建一个文件"""
# Excel_create = Workbook("test.xlsx")
# sheet = Excel_create.create_sheet("python_test")
# Excel_create.save("test.xlsx")

"""遍历列表，分别写入Excel"""
# file = load_workbook("test.xlsx")
# sheet = file.get_sheet_by_name("python_test")
# # sheet.cell(row=2,column=2).value = "two-two"
#
# for item in range(0,len(name)):
#     sheet.cell(row = 1, column = item+1).value = name[item]

"""遍历Excel，成列表打印出来"""
# file = load_workbook("test.xlsx")
# sheet = file.get_sheet_by_name("python_test")
# list_name = []
# for item in range(1,sheet.max_column + 1):
#     str = sheet.cell(row = 1,column = item).value
#     list_name.append(str)
# http://119.23.241.154:8080/futureloan/mvc/api/member/login
"""讲文件内容转换成指定格式[{},{}]"""
file = load_workbook("test.xlsx")
sheet = file.get_sheet_by_name("python_test")
params_list = []
params_dict = {}

for item in range(2,sheet.max_row+1):
    params_dict[sheet.cell(row=1,column=1).value] = sheet.cell(row=item ,column=1).value
    params_dict[sheet.cell(row=1,column=2).value] = sheet.cell(row=item, column=2).value

    params_list.append(params_dict)
print(params_list)
file.save("test.xlsx")
