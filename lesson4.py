# 根据字典中的值的大小对字典的项进行排序
stu = {'tom': 80, 'jerry': 90, 'kelly': 64, 'kimmy': 45}
# 使用sotred()
# sorted()里面传入的是可迭代对象，而字典的可迭代对象是字典的key
# 方法1：利用zip把字典转成每一对转成元组
# r = zip(stu.values(),stu.keys())
# r = sorted(r, reverse=False)
# print(r)
# 方法2：sorted()的key参数
r = sorted(stu.items(), key=lambda x:x[1],reverse=False)
print(r)

