# coding:utf-8

from openpyxl import load_workbook   # 打开工作簿
from openpyxl import Workbook   # 创建一个工作簿

"""创建一个工作簿"""
ex = Workbook("TEST11")     # 创建一个Excel
sh = ex.create_sheet("python")     # 创建一个sheet
ex.save("TEST11.xlsx")       # 保存Excel

file = load_workbook("TEST11.xlsx")    # 打开一个Excel
sheet = file.get_sheet_by_name("python")        # 确定sheet表单，定位sheet
sheet.cell(row=2,column=2).value = "two-two"  # 定位位置，来写数据（X、Y行列定位）


result = sheet.cell(row=1,column=1).value   # 查看某一单元格的数据
print(result)

row = sheet.max_row     # 统计有多少行
col = sheet.max_column  # 统计有多少列

print(row)
print(col)

file.save("TEST11.xlsx")