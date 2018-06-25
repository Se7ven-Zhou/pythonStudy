# coding : utf-8

import time
import requests

class Parameter:

    def __init__(self,admin = "!QS#$^Tghi0"):

        self.admin = admin

    def get_params(self,params = {},signature = "4caaa6567e7f32d4d4fd7027212271de"):
        parameters = {}
        parameters["admin"] = self.admin
        parameters["signature"] = signature
        parameters["timestamp"] = int(time.time()*1000)
        parameters["params"] = params

        return parameters


if __name__ == "__main__":
    url = "http://119.23.132.26:8092/meeting/getLive"
    parameter = Parameter().get_params()

    post = requests.post(url,parameter)
    print(post.json())
