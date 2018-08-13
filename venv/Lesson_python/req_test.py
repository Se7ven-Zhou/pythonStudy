# coding:utf-8

import requests

url = "http://business-dev.veehui.com/m/getLiveOrPreviewMeetingCount"
headers = {"Content-Type":"application/json"}
# json = {"startTime":"2018-01-01 00:00:00","endTime":"2018-12-31 23:59:59"}
# json = {"startTime":"","endTime":""}
json = {}
#  test = requests.request("POST",url,json=json,headers=header)
test = requests.post(url,json=json,headers=headers)

print(test.text)