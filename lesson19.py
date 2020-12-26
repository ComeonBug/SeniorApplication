# 如何读写文本文件
# python2和python3中字符串的语义发生了变化
#    python2    python3
#      str  ——》  bytes
#   unicode   ——》 str
s = '你好'
print(s.encode('utf8'))
b = b'\xe4\xbd\xa0\xe5\xa5\xbd'
print(b.decode('utf8'))