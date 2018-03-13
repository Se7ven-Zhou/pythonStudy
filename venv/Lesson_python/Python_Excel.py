# coding:utf-8

from openpyxl import load_workbook   # 打开工作簿
from openpyxl import Workbook   # 创建一个工作簿

"""创建一个工作簿"""
# ex = Workbook("hello.xlsx")     # 创建一个Excel
# sheet = ex.create_sheet("python")     # 创建一个sheet
# ex.save("hello.xlsx")       # 保存Excel

ex = load_workbook("hello.xlsx")    # 打开一个Excel
ex.get_sheet_by_name(python)        # 确定sheet表单，定位sheet
sheet        # 定位位置，来写数据（X、Y行列定位）
