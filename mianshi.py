import requests
data = [8, 10, 1, 8, 4, 9, 10, 5, 10, 5]
# 列表去重不适合用列表解析、filter之类
b = list({}.fromkeys(data).keys())
print(b)
requests.request()
