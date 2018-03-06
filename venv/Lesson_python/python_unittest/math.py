# coding:utf-8

class mathTest:

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

if __name__ == "__main__":
    result = math_test(5,6)
    print(result.add())
    print(result.sub())