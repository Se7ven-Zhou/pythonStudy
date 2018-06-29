# coding:utf-8

import os
from openpyxl import load_workbook
from openpyxl import workbook


class Read_Data:

    def __init__(self,filename,address = os.path.split(os.path.dirname(__file__))[0]+"\TestDatas"):

        self.address = address
        self.filename = filename

    def Get_Params(self):
        path = os.path.join(self.address, self.filename)
        file = load_workbook(path)
        sheet = file.get_sheet_by_name("meeting_info")

        params_list = []
        for item in range(2,sheet.max_row + 1):
            params = sheet.cell(row = item, column = 2).value
            params_list.append(params)
        file.close()
        return params_list

    def Get_API(self):
        path = os.path.join(self.address, self.filename)
        file = load_workbook(path)
        sheet = file.get_sheet_by_name("meeting_info")

        api_list = []
        for item in range(2,sheet.max_row + 1):
            api = sheet.cell(row = item,column = 1).value
            api_list.append(api)
        file.close()
        return api_list

    def Get_Code(self):
        path = os.path.join(self.address, self.filename)
        file = load_workbook(path)
        sheet = file.get_sheet_by_name("meeting_info")

        code_list = []
        for item in range(2,sheet.max_row + 1):
            code = sheet.cell(row = item,column = 3).value
            code_list.append(code)
        file.close()
        return code_list

if __name__ == "__main__":

    xx = Read_Data("test_data.xlsx").Get_Params()
    yy = Read_Data("test_data.xlsx").Get_API()
    zz = Read_Data("test_data.xlsx").Get_Code()
    print(xx[1],yy[1],zz[1])



