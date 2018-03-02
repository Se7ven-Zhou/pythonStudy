# coding:utf-8

class Teacher:
    # 属性
    name = "华华"
    age = 18
    sex = "girl"

    # 函数
    def eat(self):
        print("吃！")

    def run(self):
        print("跑！")


class student:
    def __init__(self, name, age):  # 初始化函数，创造实例的时候，传递参数
        self.xm = name
        self.xb = age

    def study_python(self):
        print(str(self.xm) + "今年" + str(self.xb) + "好好学")

    def math_add(self, a, b):
        c = int(a) + int(b)
        print("结果是" + str(c))


# tester1 = Teacher()  # 创造一个实例
# print tester1.name  # 调用类的属性
# tester1.eat()  # 调用类的函数
stu1 = student("seven", 18)  # 如果有初始化函数，实例的时候一定要传参数
stu1.study_python()


