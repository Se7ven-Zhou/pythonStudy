# coding:utf-8

"""输入一个字符串，字符大于2的，保留前两个字符"""

# def judge(name=raw_input("请输入英文名：")):
#     if len(name) > 2:
#         list_name = list(name)
#         return (str(list_name[0]) + str(list_name[1]))
#     else:
#         return name

"""传入一个字典和一个字符串，如果字符串不在字典里，就保存"""

# def check(dict, str):
#     if str in dict.values():
#         return dict
#     else:
#         dict["age"] = str
#         return dict


"""读取文件，list=[{key:value,key:value},{key:value,key:value}] 格式"""

with open("D:\\Python27\\Case\Test\\pythonStudy\\test.txt", "r") as file:
    content = file.read()
    content_list = content.split("\n")
    dict_list = []
    dict = {}

    for item in range(0, len(content_list)):
        content_split = content_list[item].split(",")
        for i in range(0, len(content_split)):
            dict_key = content_split[i][0:content_split[i].index(":")]
            dict_value = content_split[i][content_split[i].index(":") + 1:]
            dict[dict_key] = dict_value
        dict_list.append(dict)
    print dict_list

""" 龙哥代码"""
# with open("D:\\Python27\\Case\Test\\pythonStudy\\test.txt","r+") as file:
#     list_data = []
#     for li in file.readlines():
#         a = li.split(",")
#         dict_a = []
#         for di in a:
#             di_key = di[:di.index(":")]
#             di_value = di[di.index(":") + 1]
#             dict_a[di_key] = di_value
#         list_data.append(dict_a)
# print list_data

