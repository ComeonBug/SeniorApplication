# 如何在一个for语句中迭代多个可迭代对象？
# 并行：zip：把所有的可迭代对象一一对应压缩合并，个数取最少的
# 串行：itertools.chain:把所有的可迭代对象串成一个可迭代对象
from itertools import chain
# math = [63, 28, 83, 96, 54, 87, 37, 15, 30, 32]
# english = [53, 91, 23, 17, 81, 26, 22, 48, 25, 27]
# history = [53, 91, 23, 17, 81, 26, 22, 48, 25, 27]
# for i in zip(math,english,history):
#     print(i)
c1 = [63, 28, 83, 96, 54, 87, 37, 15, 30, 32]
c2 = [53, 91, 23, 17, 81, 26, 22, 48, 25, 27]
c3 = [53, 91, 23, 17, 81, 26, 22, 48, 25, 27]
count = 0
for i in chain(c1, c2, c3):
    if i > 90:
        count += 1
print(count)