# coding:utf-8

from openpyxl import load_workbook
from openpyxl import Workbook
from urllib import request
from prettytable import PrettyTable
import time


class Package_MailContent:

    def __init__(self,path):

        self.path = path

    def report_data(self):
        file = load_workbook(self.path)
        sheet = file.get_sheet_by_name("result")

        para_list =[]
        for i in range(2,sheet.max_row+1):
            pass
            data_list = []
            for j in range(1,sheet.max_column+1):
                data = sheet.cell(row=i, column=j).value
                data_list.append(data)
            para_list.append(data_list)

        file.close()
        return para_list

    def test_info(self,count,tester="Seven"):
        file = load_workbook(self.path)
        sheet = file.get_sheet_by_name("result")

        count_fail = int(sheet.max_row) - 1
        count_pass = int(count) - int(count_fail)
        if int(count_fail) ==0:
            count_passRate = "100%"
        else:
            count_passRate = int(count_pass)/int(count)

        tester = tester
        startTime = time.strftime("%Y-%m-%d_%H_%M_%S")
        result = "总共：\t"+ str(count) + "\t,\t通过：" + str(count_pass) + "\t,\t失败：" + str(count_fail) + "\t,\t通过率："+ str(count_passRate)


    def mail_content(self):

        content = report_data()
        x = PrettyTable(["name", "api", "result"])
        for i in range(len(content)):
            x.add_row(content[i])
        print(x)
        return str(x)


if __name__ == "__main__":
    pass
    # "C:/Users/Administrator/PycharmProjects/pythonStudy/venv/HuShi/Reports/2018-10-24.xlsx"




# data["1"] = sheet.cell(row=item, column=1).value

# text = ""
# # for i in range(0,len(data_list)):
# for i in range(0,len(data_list)):
#     text += "\n"
#     for j in data_list[0].keys():
#         text += str(data_list[i][j]) + "\t\t\t\t"
# print(text)

list1 = ["小明",200, 199, 198]
list2 = ["大明白",197, 196, 195]
#
# x = PrettyTable(["名字", "数学成绩", "语文成绩", "计算机成绩"])
# x.add_row(list1)
# x.add_row(list2)
# print(x)

