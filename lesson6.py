# 如何让字段有序
# tips:使用collection中的OrderedDict
# 存进去的时候顺序是什么样，再OrderedDict中的顺序就是什么样
from collections import OrderedDict
import time
import random
d = OrderedDict()
people = ["Tom","Bob","Jerry","ketty","Tiffy","Hanna","Sun"]
start = time.time()
for i in range(7):
    p = people.pop(random.randint(0,6-i))
    time.sleep(random.randint(1, 4))
    end = time.time()
    print(p, i+1, int(end-start))
    d[p] = (i+1, int(end-start))

print(d)