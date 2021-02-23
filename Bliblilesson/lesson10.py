# 如何进行反向迭代已经如何实现反向迭代
# reversed(list)
"""
l = [1,2,3,4,5]
l1 = reversed(l)
l2 = iter(l)
print(l1)
print(l2)
# 所以：正向我们去实现：__iter__方法，反向实现__reversed__方法
"""

class FloadRange:
    def __init__(self, start, end, step = 0.1):
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        t = self.start
        while t <= self.end:
            yield t
            t += self.step

    def __reversed__(self):
        t = self.start
        while t > self.end:
            yield t
            t -= self.step


for x in reversed(FloadRange(3,1,0.5)):
    print(x)

