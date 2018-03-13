# coding:utf-8

import requests

class httpRequests:
    def __init__(self,mobile,pwd,url="http://119.23.241.154:8080/futureloan/mvc/api/member/register"):
        self.url = url
        self.params = {"mobilephone":mobile,"pwd":pwd}

    def Get(self):
        result = requests.get(self.url,self.params)
        return result.json()

    def Post(self):
        result = requests.get(self.url,self.params)
        return result.json()

class Read_data:
    def read_data(self,file_path):
        with open(file_path, "r") as file:
            f = file.readlines()
            data_list = []
            for item in range(0, len(f)):
                f_list = f[item].split(",")
                file_dict = {}
                for j in range(0, len(f_list)):
                    data = f_list[j].split(":", 1)  # 切割可以输入第几个符号切割
                    file_dict[data[0]] = data[1]
                data_list.append(file_dict)
        return data_list


if __name__ == "__main__":
    # # 参数实例化
    data = Read_data()
    data_test = data.read_data("test.txt")
    # # print(data_test[0]["mobilephone"])
    # # print(data_test)
    # # 实例化运行
    for item in range(0,len(data_test)):
        print(data_test[item])
        print(data_test[item]["mobilephone"])

        # test = httpRequests(data_test[item]["mobilephone"],data_test[item]["pwd"])
        # runner = test.Get()
        # #print(item)
        # #print(data_test[0]["mobilephone"])
        # print(runner)
