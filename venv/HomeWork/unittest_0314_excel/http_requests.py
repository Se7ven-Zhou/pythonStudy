# coding:utf-8

import requests

class Http_requests:

    def __init__(self,url,params):
        self.url = url
        self.params = params

    def Get(self):
        get = requests.get(self.url,self.params)
        return get.json()

if __name__ == "__main__":
    url = "http://119.23.241.154:8080/futureloan/mvc/api/member/login"
    params = {"mobilephone":13752852018,"pwd":123456}
    test = Http_requests(url,params).Get()
    print(test)
