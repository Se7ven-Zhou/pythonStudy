# coding : utf-8

import requests
from Lesson_python.python_config.read_config import Get_data

class HttpRrequsts:

    def __init__(self,url,params):
        self.url = url
        self.params = params

    def Get(self):
        response = requests.get(self.url,self.params)
        return response.json()

    def Post(self):
        response = requests.post(self.url,self.params)
        return response.json()

if __name__ == "__main__":
    data = Get_data().Read_config("data.conf")
    url = "http://119.23.241.154:8080/futureloan/mvc/api/member/login"
    # params = {"mobilephone":13752852018,"pwd":123465}
    tester = HttpRrequsts(url,data).Get()
    # test = tester.Get()
    print(tester)