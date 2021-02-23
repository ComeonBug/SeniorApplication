# 随机列表中统计出现次数做高的3个元素，以及他们出现的次数
import re
from collections import Counter

l = [8, 10, 1, 8, 1, 9, 10, 5, 10, 5, 5, 5, 8, 2]
# d = {}.fromkeys(l,0)
# for k in d:
#     d[k] = l.count(k)
# print(d)
# x = sorted(d.items(),key=lambda t:t[1],reverse=True)
# print(x)
# 方法2：Counter
# counter对象里是一个字典样式：值:次数
# counter.most_common(3):返回最高次数的3个，按顺序排的，是一个列表，列表里是键值对的元组，键（值）：值（次数）
from collections import Counter
c = Counter(l)
print(c)
print(c.most_common(3))
# 题目2：统计文章中词频出现最高的10个词
# r = open('import_this.txt')
# ha = r.read()
# l = re.split('\W+', ha)
# c = Counter(l).most_common(10)
# print(c)
