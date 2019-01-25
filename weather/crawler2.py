"""
link1:http://mobile.weather.com.cn/js/citylist.xml
link2:http://flash.weather.com.cn/wmaps/xml/shanghai.xml
"""

import requests
from bs4 import BeautifulSoup as bs

def data(city):
    url = 'http://mobile.weather.com.cn/js/citylist.xml'
    r = requests.get(url)
    r.encoding = 'utf-8'
    soup = bs(r.text, 'html.parser')
    part = soup.find(d3 = city)
    cityid = part.get('d1')
    city_ch = part.get('d2')

    target = 'http://flash.weather.com.cn/wmaps/xml/'+ city +'.xml'
    r = requests.get(target)
    r.encoding = 'utf-8'
    soup = bs(r.text, 'html.parser')
    status = soup.find(url = cityid)
    weather = status.get('statedetailed')
    tem1 = status.get('tem1')
    tem2 = status.get('tem2')

    city_wea = {}
    city_wea['city_ch'] = city_ch
    city_wea['weather'] = weather
    city_wea['tem_max'] = tem1
    city_wea['tem_min'] = tem2

    return city_wea

if __name__=='__main__':
    city = input('city:')
    print(data(city))
