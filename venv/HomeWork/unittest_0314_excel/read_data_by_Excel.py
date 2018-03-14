# coding:utf-8

from openpyxl import load_workbook

class Read_data:

    def __init__(self,path):
        self.path = path

    def Get_data(self):
        file = load_workbook(self.path)
        sheet = file.get_sheet_by_name("python_test")
        params = {}

        for item in range(2, sheet.max_row + 1):
            params["mobilephone"] = sheet.cell(row=item, column=2).value
            params["pwd"] = sheet.cell(row=item, column=3).value
            print(params)

        file.save("test.xlsx")


if __name__ == "__main__":

    test_data = Read_data("test.xlsx").Get_data()
    print(test_data)