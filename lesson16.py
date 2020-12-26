# 如何将多个小字符串拼接成一个大的字符串
# 方法1：+、str.__add__()
# 其实【+】就是重载了str.__add__()方法
# l = ['a','fghj','qwert','vb', 1]
# s= ''
# for i in l:
#     s += str(i)
# print(s)

# 方法2：join方法
l = ['a','fghj','qwert','vb', 1]
# ''.join(str(i) for i in l)  括号里的是省略写法的生成器解析
# 其实应该是这样写：''.join((str(i) for i in l))
# 生成器解析：(str(i) for i in l)
# 这里不用列表解析的原因是节省内存开销
s = ''.join(str(i) for i in l)
print(s)
