# coding:utf-8

class Read_data:
    def __init__(self,file_path):
        self.file_path = file_path

    def get_data(self):
        with open(self.file_path, "r") as file:
            f = file.readlines()
            data_list = []
            for item in range(0, len(f)):
                f_list = f[item].split(",")
                file_dict = {}
                for j in range(0, len(f_list)):
                    data = f_list[j].split(":", 1)  # 切割可以输入第几个符号切割
                    file_dict[data[0]] = data[1]
                data_list.append(file_dict)
        return data_list

if __name__ == "__main__":
    data = Read_data("data_test.txt").get_data()
    print(data)
