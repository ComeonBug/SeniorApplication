# 文件缓冲
# 全缓冲
# f = open('./tmp/ha.txt','w'，buffering=2)
# 行缓冲
# f = open('./tmp/ha.txt','w',buffering=1)
# 无缓冲
f = open('../tmp/ha.txt', 'w', buffering=0)
f.write('*'*4093)