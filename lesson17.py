# 如何对字符串进行左、右、居中对齐
# 方法1：字符串的rjust、ljust、center
# s = 'abc'
# print(s.rjust(10, '*'))
# print(s.ljust(10, '*'))
# print(s.center(10, '*'))

# 方法2：内置的format方法
# s = 'abc'
# print(format(s, '*<10'))
# print(format(s, '*>10'))
# print(format(s, '*^10'))
stu = {
    'name':'Tom',
    'age':16,
    'phone':'15812341234',
    'address':'上海市'
}
# max()里传可迭代对象
l = max(map(len, stu))
for s in stu:
    print(s.ljust(l), ':', stu.get(s))

