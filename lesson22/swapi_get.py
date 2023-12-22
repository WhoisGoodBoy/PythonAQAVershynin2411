import requests
import json
headers = {
    'ContentType':"application/json"
}
url = 'https://swapi.dev/api/'
response = requests.get(url + 'planets/')
print(response.json())
with open('planets.json', 'w') as planets:
    json.dump(response.json(), planets, indent=4)
