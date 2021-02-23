# 如何对迭代器做切片操作？
from itertools import islice
with open('../import_this.txt') as f:
    # s = islice(f, 2, 8)
    # s = islice(f, 5, None)
    s = islice(f, 5)
    print(type(s))
    for i in s:
        print(i)