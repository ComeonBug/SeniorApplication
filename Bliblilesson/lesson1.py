import random
# 列表解析
d = [8, 10, 1, -8, 4, -9, 10, -5, -10, 5]
# 筛选出所有的正数
z = [i for i in d if i > 0]
print(z)
# 筛选出所有的偶数
o = [j for j in d if j % 2 == 0]
print(o)
# 筛选出所有的正奇数
j = [x for x in d if x % 2 == 1 and x > 0]
print(j)

# stu = {i:random.randint(50,100) for i in range(1,11)}
stu = {1: 75, 2: 81, 3: 88, 4: 60, 5: 88, 6: 51, 7: 75, 8: 99, 9: 79, 10: 59}
# 筛选出成绩大于80的同学
g = {k:v for k,v in stu.items() if v>80}
print(g)


