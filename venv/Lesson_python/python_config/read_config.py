# coding:utf-8

import configparser

class Get_data:

    def Read_config(self,path):
        data = configparser.ConfigParser()  # 创建实例
        data.read(path, encoding="utf-8")  # 读取配置文件

        mobile = eval(data.get("DATA", "mobile"))
        password = eval(data["DATA"]["pwd"])
        params = {"mobilephone":mobile,"pwd":password}
        return params

if __name__ == "__main__":
    # data = Get_data()
    # data_params = data.Read_config("data.conf")

    data = Get_data().Read_config("data.conf")
    print(data)
