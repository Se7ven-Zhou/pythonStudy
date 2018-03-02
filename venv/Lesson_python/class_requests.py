# coding:utf-8

import requests

url = "http://119.23.241.154:8080/futureloan/mvc/api/member/register"

result = requests.get(url)


# print(result.encoding)      # 查看编码
# print(result.status_code)   # 查看状态码

print(result.text)      # 查看信息
print(result.json())    # 返回Json格式（字典dict类型）