# 如何将文件映射到内存：
# 使用标准库中的mmap函数，它需要一个打开的文件描述符作为参数
import mmap


f = open('某文件','rb')
m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)