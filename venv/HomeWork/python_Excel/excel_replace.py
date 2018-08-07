#coding:utf-8

from openpyxl import Workbook
from openpyxl import load_workbook
import os


class Excel_Datas:

    def __init__(self):

        self.file_address = os.getcwd()
        self.file_name = "test.xlsx"
        self.file_path = os.path.join(self.file_address,self.file_name)

        self.file = load_workbook(self.file_path)
        self.caseData_sheet = self.file.get_sheet_by_name("caseData")
        self.initData_sheet = self.file.get_sheet_by_name("initData")

    def get_initData(self):
        init_list = {}
        init_list["${init}"] = self.initData_sheet.cell(row=1, column=2).value
        init_list["${registe}"] = int(self.initData_sheet.cell(row=1, column=2).value + 1)
        init_list["${login}"] = int(self.initData_sheet.cell(row=1, column=2).value + 2)

        return init_list

    def get_data(self):
        init_data = self.get_initData()
        request_Data_list = []
        for item in range(2,self.caseData_sheet.max_row+1):
            request_Data = {}
            request_Data["api"] = self.caseData_sheet.cell(row=item, column=1).value
            request_Data["params"] = self.caseData_sheet.cell(row=item, column=2).value

            for key,valie in range init_data.
                if request_Data["params"].find

            # request_Data_list.append(request_Data)
        print(request_Data_list)

    def update_initData(self):

        pass

    def save_file(self):

        self.file.save()

if __name__ == "__main__":

    result = Excel_Datas().get_data()
    # print(result)