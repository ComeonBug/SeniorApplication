# 如何处理二进制文件
import struct
import array

b = b'\xe4\xbd\xa0\xe5\xa5\xbd'
print(struct.unpack('h', b))
buf = array.array('h',(0 for _ in range(10)))
f = open('text.wav','r')
