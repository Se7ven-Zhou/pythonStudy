# coding:utf-8

import requests
import re

url = "http://business-dev.veehui.com/m/getLiveOrPreviewMeetingCount"
headers = {"Content-Type":"application/json"}
# json = {"startTime":"2019-01-01 00:00:00","endTime":"2018-12-31 23:59:59"}
expected_data = '{"code":"1","result":{.*今日新增预告0场.*}}'
# json = {"startTime":"22","endTime":"22"}
json = {}
#  test = requests.request("POST",url,json=json,headers=header)
test = requests.request("POST",url,json=json,headers=headers)
a = "abc"
b = "xyz"
try:
    assert test.json()["code"] == "1",print(a)
except Exception as error:
    print("断言失败3")
    if test.json()["status"] == 500:
        a = "xyz"
        print(a)
        print("断言失败4")
        print("断言失败5")
    raise error
"""正则匹配"""
# if re.match(expected_data,test.text) is not None:  # 可用self.assertIsNotNone()方法
#     print("匹配成功")
# else:
#     print("匹配失败")

print(test.text)
#
# url = "http://39.108.16.93:20012/secure/QuickCreateIssue.jspa?decorator=none"
# headers = {"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
#            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0",
#            "Cookie": "atlassian.xsrf.token=BQGC-6ARB-IN3M-2T50_cea041428c5f8cf318993c1f475bf2d6c28ee790_lin; JSESSIONID=8A8316DAAA72B844FE5162E737799357; jira.editor.user.mode=wysiwyg; seraph.rememberme.cookie=10317%3Ac1f4ec7aa9ab9e0d9b6e701a641af566b19a98bd",
#            "X-AUSERNAME": "zhouj",
#            "Connection": "keep-alive"
#            }
# params = {"pid":"10005",
#           "issuetype":10004,
#           "atl_token":"BQGC-6ARB-IN3M-2T50_cea041428c5f8cf318993c1f475bf2d6c28ee790_lin",
#           "formToken":"fc5df7e565d1da57a4250186cb3d422e6bcf96fe",
#           "summary":"【BUG】自动化提交问题-Test",
#           "description":"est",
#           "priority":3,
#           "environment":"",
#           "dnd-dropzone":"",
#           "issuelinks	issuelinks":"",
#           "issuelinks-linktype":"blocks",
#           "assignee":"zhouj",
#           "customfield_10101":"",
#           "fieldsToRetain":"project",
#           "fieldsToRetain":"issuetype",
#           "fieldsToRetain":"components",
#           "fieldsToRetain":"fixVersions",
#           "fieldsToRetain":"priority",
#           "fieldsToRetain":"labels",
#           "fieldsToRetain":"environment",
#           "fieldsToRetain":"versions",
#           "fieldsToRetain":"issuelinks",
#           "fieldsToRetain":"assignee",
#           "fieldsToRetain":"customfield_10102",
#           "fieldsToRetain":"customfield_10101}"
#           }
# test = requests.post(url,params,headers=headers)
# print(test.text)
# json = {"startTime":"2019-01-01 00:00:00","endTime":"2018-12-31 23:59:59"}
# expected_data = '{"code":"1","result":{.*今日新增预告0场.*}}'


