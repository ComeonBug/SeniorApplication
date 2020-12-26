import random

cor = random.randint(1, 100)


def guess(num):
    if num == cor:
        print('正确')
        return 1
    elif num > cor:
        print("大了")
        return 0
    else:
        print("小了")
        return 0


while True:
    num = input("请输入猜的数：")
    try:
        num = int(num)
        res = guess(num)
        if res == 1:
            break
    except Exception as e:
        print("不要输入非数字哦，请重新输入数字：")
