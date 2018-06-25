# coding :utf-8

import requests
from HuShi.Config import Environment
from HuShi.Public.parameter import Parameter

class Login:

    def __init__(self,unionId,openId,accessToken = "11_MEY6Ubmfc6qcuz-W1Q7BYOcvXJp7dobyKYiQgJxtU0SA8f25edJTh4pKe9GZus7n102m9Jx7ivN0LqWz1wELlYDTeIjONYOx2XyLdv3JYOw",systemName = "Android|8681-A01;5.1;22"):

        self.openId = openId
        self.unionId = unionId
        self.accessToken = accessToken
        self.systemName = systemName

    def Login_APP(self,address):

        params = {}
        params["openId"] = self.openId
        params["unionId"] = self.unionId
        params["accessToken"] = self.accessToken
        params["systemName"] = self.systemName

        # 组装参数
        parameters = Parameter().get_params(params)

        api = "/u/loginByWechat"
        url = address + api
        print(parameters)
        post = requests.post(url,parameters)
        return post.json()


if __name__ == "__main__":
    address = Environment().Test()
    result = Login("o1WVZwxbvXmbZDgshqyxep4KhehE","owG8P08gTbda-maVestQIW9J50Og").Login_APP(address)
    print(result)
