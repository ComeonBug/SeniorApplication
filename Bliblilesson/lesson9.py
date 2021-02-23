# topic：使用生成器实现可迭代对象

# 生成器:generator
# yield
# 生成器和迭代器都支持next方法
'''
# g.__iter__()的结果也是一个生成器
def f():
    print('in f(), 1')
    yield 1

    print('in f(), 2')
    yield 2

    print('in f(), 3')
    yield 3

g = f()
n = next(g)
print(n)
'''



class PrimeNumbers:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def isPrimeNum(self, k):
        if k < 2:
            return False
        for i in range(2, k):
            if k % i == 0:
                return False
        return True

    def __iter__(self):
        for k in range(self.start, self.end + 1):
            if self.isPrimeNum(k):
                yield k


p = PrimeNumbers(1,10)
for x in p:
    print(x)

