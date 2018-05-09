# coding:utf-8

import requests
import time
import unittest
class Http_requests:

    def __init__(self,url,params,):
        self.url = url
        self.params = params

    def Post(self):
        post = requests.post(self.url,self.params)
        return post.json()

if __name__ == "__main__":
    url = "http://119.23.132.26:8091/u/login"
    params = {"params":"{'mobile':'13752852015','password':'123456','systemName':'IOS'}","signature":"82601564dc52a8e456f7c82272ba3d09","timestamp":1522305160,"admin":"!QS#$^Tghi0"}
    test = Http_requests(url,params).Post()
    print(test)
