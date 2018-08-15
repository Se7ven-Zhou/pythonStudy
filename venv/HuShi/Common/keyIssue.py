# coding:utf-8

import requests
import HuShi.Config.jiraBug_config

class KeyIssue:

    def __init__(self,summary,description):

        self.params = {"pid":"10005",
                  "issuetype":10004,
                  "atl_token":"BQGC-6ARB-IN3M-2T50_cea041428c5f8cf318993c1f475bf2d6c28ee790_lin",
                  "formToken":"fc5df7e565d1da57a4250186cb3d422e6bcf96fe",
                  "summary":summary,
                  "description":description,
                  "priority":3,
                  "environment":"",
                  "dnd-dropzone":"",
                  "issuelinks	issuelinks":"",
                  "issuelinks-linktype":"blocks",
                  "assignee":"zhangwj",
                  "customfield_10101":"",
                  "fieldsToRetain":"project",
                  "fieldsToRetain":"issuetype",
                  "fieldsToRetain":"components",
                  "fieldsToRetain":"fixVersions",
                  "fieldsToRetain":"priority",
                  "fieldsToRetain":"labels",
                  "fieldsToRetain":"environment",
                  "fieldsToRetain":"versions",
                  "fieldsToRetain":"issuelinks",
                  "fieldsToRetain":"assignee",
                  "fieldsToRetain":"customfield_10102",
                  "fieldsToRetain":"customfield_10101}"
                  }
        self.url = HuShi.Config.jiraBug_config.url
        self.headers = HuShi.Config.jiraBug_config.headers

    def Commit(self):

        result = requests.post(self.url,self.params,headers=self.headers)