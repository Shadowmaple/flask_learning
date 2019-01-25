import requests
from bs4 import BeautifulSoup as bs

key = input('城市:')
target = 'http://mobile.weather.com.cn/js/citylist.xml'
r = requests.get(target)
r.encoding='utf-8'
soup = bs(r.content, 'html.parser')
cityid = soup.find(d2 = key)['d1']

url = 'http://www.weather.com.cn/data/sk/'+ cityid +'.html'
r = requests.get(url)
r.encoding = 'utf-8'
part = r.json().get('weatherinfo')
city = part.get('city')
temp = part.get('temp')
wind = part.get('WD')

print(city,temp,wind)

