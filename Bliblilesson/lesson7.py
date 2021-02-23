# 如何实现用户浏览的历史记录的功能
# tips:
# 使用collections.deque来存历史，deque是一个双端循环列表
# 初始化一个空的长度为5的列表：d = deque([],5)
# d.append(x):把x添加到d中，如果已经有5个来，最前面的1个将会被顶出去
# 在使用pickle.dump()来把对象存储到文件中
# 如果业务需要，还可以从文件中读取出对象：pickle.load()

import random
from collections import deque
import pickle

cor = random.randint(1, 100)
d = deque([], 5)


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
        d.append(num)
        pickle.dump(d, open('history.txt', 'wb'))
        res = guess(num)
        if res == 1:
            break

    except Exception as e:
        if num == 'history' or num == 'h?':
            print(list(d))
        else:
            print("不要输入非数字哦，请重新输入数字：")

