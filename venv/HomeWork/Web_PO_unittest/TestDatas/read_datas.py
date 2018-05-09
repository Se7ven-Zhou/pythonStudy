# coding:utf-8

from openpyxl import load_workbook
import os

class Read_data:

    def __init__(self,file_name):

        self.file_name = file_name

    def Read_login_success(self,sheet_name):
        address = os.path.dirname(__file__)
        file_path = os.path.join(address,self.file_name)
        file =load_workbook(file_path)
        sheet = file.get_sheet_by_name(sheet_name)
        print(file_path)
        print(address)
        data_list = []
        for item in range(2,sheet.max_row + 1):

            login_data = {}
            login_data["mobile"] = sheet.cell(row=item,column = 1).value
            login_data["password"] = sheet.cell(row=item,column = 2).value
            login_data["nickname"] = sheet.cell(row=item,column = 3).value
            data_list.append(login_data)
        return data_list

if __name__ == "__main__":
   data = Read_data("Login_Data.xlsx").Read_login_success("login_success")
   print(data)