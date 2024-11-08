import requests
import json
base_url="https://api.chucknorris.io/jokes/random"
response=requests.get(base_url)
joke=response.json()
#print(json.dumps(joke, indent=2))
print(joke['value'])
