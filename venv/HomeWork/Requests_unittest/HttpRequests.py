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

if __name__ == "__main__":
    test = httpRequests("13752852018","123456")
    runner = test.Get()
    print(runner)