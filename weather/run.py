from flask import Flask
abc = Flask(__name__)

from crawler2 import data


@abc.route('/')
def index():
    return 'Hello, world!'

@abc.route('/<city>', methods=['GET', 'POST'])
def weather(city):
    weather = data(city)
    state = weather.get('weather')
    city_ch = weather['city_ch']
    tem = weather.get('tem_min')+'~'+weather.get('tem_max') + '摄氏度'
    return city_ch +" " +state + ' ' + tem

#weather.get('weather')+''+weather.get('tem_min')+'~'+weather.get('tem_max')

if __name__ == '__main__':
    abc.run()

