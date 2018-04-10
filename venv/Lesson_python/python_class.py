# coding:utf-8

class Teacher:

    # 函数
    def eat(self,food):
        print("老师吃"+food)

    def run(self):
        print("跑！")

class Student(Teacher):
    def __init__(self, name, age):  # 初始化函数，创造实例的时候，传递参数
        self.xm = name
        self.xb = age

    def eat(self,food,weight):
        super(Student, self).eat(food)
        print(self.xm+"也吃，长肉"+ str(weight))

    def study_python(self):
        print(str(self.xm) + "今年" + str(self.xb) + "好好学")

    def math_add(self, a, b):
        c = int(a) + int(b)
        print("结果是" + str(c))

# tester1 = Teacher()  # 创造一个实例
# print tester1.name  # 调用类的属性
# tester1.eat()  # 调用类的函数
# stu1 = student("seven", 18)  # 如果有初始化函数，实例的时候一定要传参数
# stu1.study_python()

stu2 = Student("seven",20).eat("water",7)
