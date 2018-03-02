# coding:utf-8

"""
格式：
try:

except Exception as e: # Exception 是捕捉所有基类错误
    print e # 打印异常
    raise e # 抛出异常，但不影响程序继续进行（为了写测试报告时，指出这是个错误）

finally:
    file.close()  # 意思是不管前面怎么样，都要执行finally里面的语句
"""

"""
上下文管理器：
with open(path,'a+') as file:   # 打开一个文件存放在file变量里
    file.write("abc")           # 代码运行完自动关闭，结束
"""

def score():
    try:
        s = input("请输入分数：")
        if int(s) >= 60:
            print("恭喜你及格了！")
        else:
            print("很遗憾，你没有及格！")
    except Exception as e:
        print(e)
        raise e
score()