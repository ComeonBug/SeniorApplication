# 如何使用临时文件？
# tempfile下的:
# emporaryFile:
# NamedTemporaryFile:创建一个带名字的

from tempfile import TemporaryFile, NamedTemporaryFile

f = TemporaryFile()
f.write(b'abcdef')
f.seek(0)
print(f.read(2))

fn = NamedTemporaryFile()
print(fn.name)
# NamedTemporaryFile(delete=False) 不会被垃圾回收
fnd = NamedTemporaryFile(delete=False)
