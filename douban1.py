import requests
from bs4 import BeautifulSoup as bs
from flask import Flask

url = 'https://book.douban.com/top250'
UserAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
res = requests.get(url, headers={'User-Agent': UserAgent}).text
bs(res, 'html.parser').find_all('div', attrs={'class':"pl2"})


app = Flask(__name__)
@app.route('/')
def hello():
    return 'hello world!'