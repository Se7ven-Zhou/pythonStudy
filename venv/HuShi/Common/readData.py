# coding:utf-8

import os
from openpyxl import load_workbook
from openpyxl import workbook


class Read_Data:

    def __init__(self,address = os.path.split(os.getcwd())[0]+"\TestDatas"):

        self.address = address

    def Get_Data(self,filename):
        path  = os.path.join(self.address,filename)
        file = load_workbook(path)
        sheet = file.get_sheet_by_name("meeting_info")

        get_info = []

        # sheet.cell(row=item, column=1).value
        params = {}
        for item in range(2,sheet.max_row + 1):
            params["id"] = sheet.cell(row = item, column = 1).value
            params["title"] = sheet.cell(row = item, column = 2).value
            get_info.append(params)

        file.close()
        return get_info

if __name__ == "__main__":

    Read_Data().Get_Data("test_data.xlsx")




