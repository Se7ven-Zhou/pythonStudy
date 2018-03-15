# coding:utf-8

import os
from openpyxl import Workbook
from openpyxl import load_workbook


class Write_excel:
    def __init__(self,address,file_name):
        self.address = address
        self.file_name = file_name

    def Write(self):
        # address = os.getcwd()
        # file_name = "test.xlsx"
        file_path = os.path.join(self.address, self.file_name)

        info_list = ["学号", "姓名", "性别", "班级"]

        if os.path.exists(file_path):
            file_excel = load_workbook(file_path)
            sheet = file_excel.get_sheet_by_name("python_test")
            for item in range(0, len(info_list)):
                sheet.cell(row=1, column=item + 1).value = info_list[item]
            file_excel.save(self.file_name)
        else:
            file_create = Workbook(file_path)
            sheet_create = file_create.create_sheet("python_test")
            file_create.save(self.file_name)
            # file_excel = load_workbook(file_path)
            # sheet = file_excel.get_sheet_by_name("python_test")
            # for item in range(0, len(info_list)):
            #     sheet.cell(row=1, column=item + 1).value = info_list[item]
            # file_create.save(self.file_name)

if __name__ == "__main__":
    address = os.getcwd()
    file_name = "test2.xlsx"
    Write_excel(address,file_name).Write()
