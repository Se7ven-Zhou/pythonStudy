# coding:utf-8

# def Judge():
#     while True:
#         try:
#             score = input("请输入分数:")
#             if 60 <= int(score) <= 100:
#                 print("及格")
#                 break
#             elif 0 <= int(score) < 60:
#                 print("不及格")
#                 break
#             else:
#                 print("成绩输入范围有误")
#                 break
#         except Exception as e:
#             print("输入的格式有误，请重新输入！")
#             print("错误是：%s"%e)
#             continue
# Judge()


"""自动贩卖机"""
"""
1.输入要的商品（定义产品以及价格）
2.输入钱币（只接受1,5,10）
3.判断金额大小
4.找零
"""
def AutoBuy(select):
    goods = {"orange":3.5, "coconut":4.0, "water":2.0, "milk":4.5}
    Sum = 0.0
    balance = 0.0
    while True:
        money = input("请投入钱币(仅限1/5/10元)：")
        if int(money)==1 or int(money)==5 or int(money)==10:
            Sum += float(money)
            if float(Sum) >= goods[select]:
                balance = float(Sum)-goods[select]
                break
            else:
                print("金额不够，请继续投币！！！")
        else:
            print ("请投入1/5/10元！！！")
    return balance

select = input("请选择购买的商品(orange/coconut/water/milk)：")
final = AutoBuy(select)
print("购买" + str(select) + '成功，找零：' + str(final))