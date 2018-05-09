# coding:utf-8

import configparser
from openpyxl import load_workbook

class Get_data:

    def __init__(self,systemName="IOS",timestamp=1522305160,signature="82601564dc52a8e456f7c82272ba3d09",admin="!QS#$^Tghi0"):
        self.systemName = systemName
        self.timestamp =timestamp
        self.signature = signature
        self.admin = admin

    def Read_config(self,path):
        data = configparser.ConfigParser()  # 创建实例
        data.read(path, encoding="utf-8")  # 读取配置文件

        ip = data.get("ADDRESS","ip")
        port = data["ADDRESS"]["port"]
        api = data["ADDRESS"]["api"]
        url = "http://"+ ip + ":" + port + api
        return url

    def Read_excel(self,path):
        file = load_workbook(path)
        sheet = file.get_sheet_by_name("python_test")
        test_data_list = []

        for item in range(2, sheet.max_row + 1):
            data_params = {}
            params = {}
            data_params["mobile"] = sheet.cell(row=item, column=1).value
            data_params["password"] = sheet.cell(row=item, column=2).value
            data_params["systemName"] = self.systemName

            params["params"] = str(data_params)
            params["timestamp"] = self.timestamp
            params["signature"] = self.signature
            params["admin"] = self.admin
            file.save(path)

            test_data_list.append(params)
        return test_data_list
        file.save("test.xlsx")

if __name__ == "__main__":
    data_url = Get_data().Read_config("test.conf")
    print(data_url)
    data_params = Get_data().Read_excel("test.xlsx")
    print(data_params)
