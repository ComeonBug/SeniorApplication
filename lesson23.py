# 如何获取文件的状态？
# 方法1：os模块：stat、fstat、lstat
# import os
# import stat
# import time
# s = os.stat('./tmp/ha.txt')
# print(s)
# # stat.S_ISDIR是否是一个目录
# print(stat.S_ISDIR(s.st_mode))
# # stat.S_ISREG是否是一个普通文件
# print(stat.S_ISREG(s.st_mode))
# # 访问权限，也在st_mode里
# print(s.st_mode & stat.S_IRUSR)
# # 获取文件时间
# print(time.localtime(s.st_atime))
# # 获取文件大小
# print(s.st_size)
# f = open('./tmp/ha.txt','r')
# fs = os.fstat(f.fileno())
# print(fs)


# 方法2：os模块的os.path函数
import os
import time
# 是否是一个文件
print(os.path.isfile('./tmp/ha.txt'))
# 文件访问时间
print(time.localtime(os.path.getatime('./tmp/ha.txt')))
# 文件大小
print(os.path.getsize('./tmp/ha.txt'))

