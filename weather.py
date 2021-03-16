from requests import get
from datetime import datetime

week = {0: 'Пнд', 1: 'Втр', 2: 'Срд', 3:'Чтв', 4:'Птн', 5:'Cбт', 6: 'Вск'}

api_url = 'http://api.openweathermap.org/data/2.5/forecast/daily'

params = {
    'q': 'Krasnodar',
    'cnt': '16',
    'appid': '11c0d3dc6093f7442898ee49d2430d20',
    'units': 'metric',
    'lang': 'ru'
}

res = get(api_url, params)
data = res.json()

print(data['city']['name'], '\t', 'Восход:', datetime.utcfromtimestamp(data['list'][0]['sunrise']+10800).strftime('%H:%M'), '\t', 'Закат:', datetime.utcfromtimestamp(data['list'][0]['sunset']+10800).strftime('%H:%M'), end = '\n\n')

print('Дата:\t\tДнем:\tНочью:\tмм:\tм/с:')

for i in data['list']:
    precip = 0
    if 'rain' in i:
        precip += i['rain']
    if 'snow' in i:
        precip += i['snow']
    print(datetime.utcfromtimestamp(i['dt']+10800).strftime('%m-%d'),' ', week[datetime.utcfromtimestamp(i['dt']+10800).weekday()], '\t', round(i['temp']['day']), '\t', round(i['temp']['night']), ' \t', round(precip,1), '\t', round(i['speed']), '\t', i['weather'][0]['description'].capitalize(), sep = '')
    if datetime.utcfromtimestamp(i['dt']+10800).weekday() == 6:
        print()
input()
