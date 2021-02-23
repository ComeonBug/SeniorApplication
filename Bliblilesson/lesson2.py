# 如何为元组中的每个元素命名，提高程序的可读性
# 每个学生的信息是一个元组，元组的好处：不可变、存储空间少，但是每次都用索引访问的话程序可读性很差
# 解决方案1：定义类似枚举类型，就是定义一些列的常量值
# name,age,sex,pho = range(4)
# stu = ('tom',17,'male','15812341234')
# print(stu[name])
# print(stu[age])
# print(stu[sex])
# print(stu[pho])
# 解决方案2：使用标准库里的colections.namedtuple
from collections import namedtuple
student = namedtuple('student',['name','age','sex','pho'])
s1 = student('tom',17,'male','15812341234')
print(s1.name)
print(s1.sex)
print(s1.age)
print(s1.pho)
s2 = student('jerry',15,'Female','15811111234')
print(s2)
