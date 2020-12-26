# 如何判断字符串已某一字母开头或者结尾？
# s = 'sdfghjkrtyuiop'
# x = s.startswith('sdf')
# print(x)
# endwith() suffix can also be a tuple of strings to try.
# e = s.endswith('p')
# print(e)
import os, stat

l = os.listdir('./tmp')
for s in l:
    if s.endswith('.py'):
        os.chmod(f'./tmp/{s}', os.stat(f'./tmp/{s}').st_mode | stat.S_IXOTH)
