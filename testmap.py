from functools import reduce

l = [8, 10, 1, -8, 4, -9, 10, -5, -10, 5]
l1 = [1, 2, 3]


def x(num):
    if num > 0:
        return num


def double_num(num):
    return num * 2


ml = map(x, l)
m2 = map(double_num, l1)
f1 = filter(x, l)
# print(list(f1))
# print(list(ml))
# map(函数,可迭代对象)：返回可迭代对象的每一个元素传入这个函数后的返回值，
# map函数的返回值是一个map对象的迭代器，需要的话可以转成list
# 所以不论这个fun是什么样的函数，这个map函数的结果map对象的元素个数==可迭代对象的元素个数
# 遮掩map适合的场景是：对可迭代对象进行一些统一的处理，【处理】，而不是【过滤】，因为它的结果格式和可迭代对象一样样啊
# 切忌：map(fun,inter_object)：其中的fun只写函数名，千万千万不要加()
# 处理的话，就比较适合：统一的比如/2，在比如一些统一的方法：
# s1 = {'d': 3, 'a': 2, 'b': 2}
# s2 = {'a': 4, 'f': 2, 'b': 2}
# s3 = {'e': 4, 'd': 4, 'b': 3}
# ms = map(lambda x:x.pop('b'), [s1, s2, s3])
# print(list(ms))

# filter:重点在过滤
# filter(fun, inter_object)：会过滤调所有使得fun返回值为false的inter_object元素，只保留为真的元素
# 它的重点是【过滤】【过滤】【过滤】
# filter函数返回也是一个filter对象的迭代器，可以转成list
# 面试题：返回列表中所有的偶数
# ll = [8, 10, 1, 4, 10, 5]
# l2 = list(filter(lambda x: x % 2 == 0, ll))
# print(l2)

# reduce(fun,inter_object)：把inter_object的第一个元素和第二个元素传给fun，fun函数返回一个值，
# 然后把这个值和inter_object的第三个元素再传给fun函数，fun函数再返回一个值
# 然后再把这个值和inter_object的第4个元素传给fun函数，一次类推，直到最后一个元素遍历完
# 特别适合做全量的加、乘这样的运算
ll = [0, 1, 2, 3, 4]
sum = 0


def sum_num(num1, num2):
    return num1 + num2


ls = reduce(sum_num, ll)
print(ls)
