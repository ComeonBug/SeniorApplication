import time


# import random
# data = [random.randint(-10,10) for _ in range(10)]


def cast_time(fun):
    def c_time(*args, **kwargs):
        start = time.time()
        fun(*args, **kwargs)
        end = time.time()
        print(f'{fun.__name__}花费的时间是：{end - start}')

    return c_time


@cast_time
def for_inter_cast(data):
    res = []
    for i in data:
        if i > 0:
            res.append(i)
    print(res)


@cast_time
def liebiaojiexi(data):
    res = [i for i in data if i > 0]
    print(res)


@cast_time
def filter_cast(data):
    res = filter(lambda x: x > 0, data)
    res = list(res)
    print(res)


if __name__ == '__main__':
    data = [8, 10, 1, -8, 4, -9, 10, -5, -10, 5]
    for_inter_cast(data)
    liebiaojiexi(data)
    filter_cast(data)
