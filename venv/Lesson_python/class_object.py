# coding:utf-8

"""类的继承"""


class Father:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self, c, d):
        return c + d

    def sub(self):
        return self.a - self.b

    def Print(self):
        print("这是父类，打印a+b=%s" % self.a + self.b)


class Mother:

    def Mul(self, c, d):
        return c*d


class son(Father):  # 继承father类全部属性和函数
    def div(self):  # 子类可以自己添加函数
        return self.a / self.b

    def sub(self):  # 子类可以修改父类的函数
        print("这是子类:" + str(self.a - self.b))

    def Print(self):
        super(son, self).Print()  # 超继承


if __name__ == "__main__":      # 函数执行的入口
    stu1 = son(6, 2)
    stu1.sub()
    stu2 = Father(6, 2)
    print stu2.sub()
