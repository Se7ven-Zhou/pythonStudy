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

# with open("zj.txt", "r") as file:
#     content = file.read()
#     content_list = content.split("\n")
#     dict_list = []
#     dict = {}
#
#     for item in range(0, len(content_list)):
#         content_split = content_list[item].split(",")
#         print(content_split)
#         for i in range(0, len(content_split)):
#             # print(content_split[i])
#             dict_key = content_split[i][0:content_split[i].index(":")]
#             dict_value = content_split[i][content_split[i].index(":") + 1:]
#             dict[dict_key] = dict_value
#         dict_list.append(dict)
#     print(dict_list)


with open("zj.txt","r") as file:
    f = file.readlines()
    data_list =[]
    for item in range(0,len(f)):
        f_list = f[item].split(",")
        file_dict = {}
        for j in range(0,len(f_list)):
            data = f_list[j].split(":",1) # 切割可以输入第几个符号切割
            file_dict[data[0]] = data[1]
        # print(file_dict)
        data_list.append(file_dict)
    print(data_list)
#
# print(data_list[0]["url"])

# class Read_data:
#     def read_data(self,file_path):
#         with open(file_path, "r") as file:
#             f = file.readlines()
#             data_list = []
#             file_dict = {}
#             for item in range(0, len(f)):
#                 f_list = f[item].split(",")
#                 # print(f_list)
#                 for j in range(0, len(f_list)):
#                     data = f_list[j].split(":", 1)  # 切割可以输入第几个符号切割
#                     file_dict[data[0]] = data[1]
#                 data_list.append(file_dict)
#         return data_list
#
# sl = Read_data()
# tt = sl.read_data("zj.txt")
# print(tt)