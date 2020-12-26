# 惰性访问时建议使用迭代器｜迭代对象
# 可迭代对象：有__iter__方法
# 迭代器对象：有next方法
# 可以生成一个迭代器
# for语句迭代的是是一个可迭代对象
# 由可迭代对象得到迭代器
# iter(可迭代对象)——》这样就生成了一个迭代器
# __iter__是一个迭代协议
# 可迭代对象都有__iter__这个方法
# iter(对象)就等于调用这个对象的__iter__方法，如果找不到__iter__的话，就去找__getitem__方法
# python3中取消了python2里：迭代器.next()的方式，换成了next(迭代器)这样的全局的方法
#
from collections import Iterable,Iterator
import requests


class WetherIterator(Iterator):
    def __init__(self,cities):
        self.cities = cities
        self.index = 0

    def getWeather(self,city):
        r = requests.get('http://t.weather.sojson.com/api/weather/city/101030100')
        data = r.json()['data']['wendu']
        return data

    def next(self):
        if self.index == len(self.cities):
            raise StopIteration
        city = self.cities[self.index]
        self.index+=1
        return self.getWeather(city)


class WeatherIterable(Iterable):
    def __init__(self,cities):
        self.cities = cities

    def __iter__(self):
        return WeatherIterable(self.cities)

for x  in WeatherIterable(['北京','上海']):
    print(x)

