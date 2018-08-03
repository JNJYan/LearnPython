from urllib.request import urlretrieve
import requests
from bs4 import BeautifulSoup
from os import remove
import http.cookiejar as cookielib
from PIL import Image

url = 'https://accounts.douban.com'
login_url = url + '/login'
datas = {
    'remember':'on',
    'source':'movie'
}

headers = {
    'Host':'www.douban.com',
    'Referer':'https://www.douban.com/',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'zh-CN,zh;q=0.9'
}