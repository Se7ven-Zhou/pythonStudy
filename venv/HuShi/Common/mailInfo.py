# coding:utf-8

from openpyxl import load_workbook
from openpyxl import Workbook
from urllib import request
from prettytable import PrettyTable
import time,os
from pyquery import PyQuery as pq


class MailInfo:

    def __init__(self, path):

        self.path = path

    def GetErrorData(self):
        file = load_workbook(self.path)
        sheet = file.get_sheet_by_name("result")

        para_list = []
        for i in range(2, sheet.max_row + 1):
            pass
            data_list = []
            for j in range(1, sheet.max_column + 1):
                data = sheet.cell(row=i, column=j).value
                data_list.append(data)
            para_list.append(data_list)

        file.close()

        x = PrettyTable(["name", "api", "result"])
        for i in range(len(para_list)):
            x.add_row(para_list[i])
        return (str(x))


    def GetInfo(self, count, tester="Seven"):
        file = load_workbook(self.path)
        sheet = file.get_sheet_by_name("result")

        count_fail = int(sheet.max_row) - 1
        count_pass = int(count) - int(count_fail)

        if int(count_fail) == 0:
            count_passRate = 1
        else:
            count_passRate = int(count_pass) / int(count)

        info = ("""<div class='heading'>
<h1 style="font-family: Microsoft YaHei">Requests_AutoTest</h1>
<p class='attribute'><strong>测试人员 : </strong> Seven</p>
<p class='attribute'><strong>测试时间 : </strong>{}</p>
<p class='attribute'><strong>合计耗时 : </strong> 0:00:21.371223</p>
<p class='attribute'><strong>测试结果 : </strong> 共 {}，通过 {}，失败 {}，通过率= {:.2%}</p>
<p class='description'></p>
</div>""".format(time.strftime("%Y-%m-%d %H:%M:%S"), count, count_pass, count_fail, count_passRate))

        file.close()
        return info

    def GetAttach(self):
        address = os.path.split(os.path.dirname(__file__))[0] + "\Reports"
        list = os.listdir(address)
        print(list)


if __name__ == "__main__":
    path = "C:/Users/Administrator/PycharmProjects/pythonStudy/venv/HuShi/Reports/2018-10-24.xlsx"
    # test = Package_MailContent(path).test_info(5)
    # print(test)
    MailInfo().GetAttach()
