# coding:utf-8

import requests
import re

url = "http://business-dev.veehui.com/m/getLiveOrPreviewMeetingCount"
headers = {"Content-Type":"application/json"}
json = {"startTime":"2018-01-01 00:00:00","endTime":"2018-12-31 23:59:59"}
expected_data = '{"code":"1","result":{.*今日新增预告0场.*}}'
# json = {"startTime":"","endTime":""}
# json = {}
#  test = requests.request("POST",url,json=json,headers=header)
test = requests.post(url,json=json,headers=headers)
if re.match(expected_data,test.text) is not None:  # 可用self.assertIsNotNone()方法
    print("匹配成功")
else:
    print("匹配失败")
# print(type(test.json()["result"]["newPreviewCount"]))
# print(type())


# print(test.json())