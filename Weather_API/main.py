##needs the api key, not provided for obvious reasons ;)
import datetime as dt
import requests

BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?'
API_KEY = open('api_key.txt', 'r').read()
CITY = 'Aberdeen'

url = BASE_URL + 'appid=' + API_KEY + '&q=' + CITY


response = requests.get(url).json()

print(response)
