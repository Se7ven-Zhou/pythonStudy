# coding = utf-8

import time,os

# class GetLatestReport:
#
#     def New_report(self):
address = os.path.split(os.path.dirname(__file__))[0] + "\Reports"
dir_list = os.listdir(address)
dir_list = sorted(dir_list, key=lambda x: os.path.getmtime(os.path.join(address, x)))
print(dir_list[-1])