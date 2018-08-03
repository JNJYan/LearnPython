import requests
from bs4 import BeautifulSoup


url_host = 'https://www.qiushibaike.com'
url = url_host + '/text/page/1'

user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'

headers = {
    'User-Agent': user_agent,
}

r = requests.get(url, headers=headers)
# print(r.text)
soup = BeautifulSoup(r.text, 'xml')
a_soups = soup.find_all('a', attrs={'class':'contentHerf'})
for a in a_soups:
    print(a.get('href'))
