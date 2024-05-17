import requests
import json

host = 'data.usajobs.gov';  
#userAgent = 'email@address.com';   "User-Agent":userAgent,

BASE_URL = 'https://data.usajobs.gov/api/search'
API_KEY = open('api_key.txt', 'r').read()
CITY = 'Aberdeen'

response = requests.get(BASE_URL, headers={"Host":host,  "Authorization-Key":API_KEY}).json()

with open('output.txt', 'w') as convert_file: 
     convert_file.write(json.dumps(response))
