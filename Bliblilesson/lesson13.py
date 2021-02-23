# 如何拆分含有多种分割符的字符串
# 方法1：
# def my_split(s, ds):
#     res = [s]
#     for d in ds:
#         t = []
#         # map(lambda i: t.extend(i.split(d)), res) # 这句貌似在python3中不生效
#         for i in res:
#             t.extend(i.split(d))
#         res = t
#     return [x for x in res if x]
#
#
# s = 'df,,ghj;kl,DF|GH\tJdfghjk;'
# print(my_split(s, ',;|\t'))

# 方法2：正则
import re
s = 'df,,ghj;kl,DF|GH\tJdfghjk;'
l = re.split(r'[,;|\t]+', s)
print(l)

