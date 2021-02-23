# 找到几个字典中的公共键
from functools import reduce
from random import randint,sample
s1 = {'d': 3, 'a': 2, 'b': 2}
s2 = {'a': 4, 'f': 2, 'b': 2}
s3 = {'e': 4, 'd': 4, 'b': 3}
# s2 = {x:randint(1,4) for x in sample('abcdef',3)}
# 方法1:
# res = []
# for i in s1:
#     if i in s2 and i in s3:
#         res.append(i)
# print(res)
# 方法2：集合互相与操作，就能得到交集
# ha = map(dict.keys,[s1, s2, s3])
# res = reduce(lambda a,b:a & b, ha)
# print(res)
s11 = set(s1.keys())
s22 = set(s2.keys())
s33 = set(s3.keys())
s = s11 & s22 & s33
print(s)
reduce(lambda a, b: a & b, map(dict.keys, [s1, s2, s3]))