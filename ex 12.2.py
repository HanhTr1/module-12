import requests
import json
from pint import UnitRegistry
city_name=input("Enter city name: ")
api_key= "f540fba3af1f42b63f4f4669d3d52443"
url=f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
response = requests.get(url)
print(json.dumps(response.json(),indent=2))
for data in response.json()['weather']:
    print(data['main'])
    print(data['description'])
convert = UnitRegistry()
temp = response.json()['main']['temp']
kelvin_temp= temp * convert.kelvin
celsius_temp = kelvin_temp.to(convert.celsius)
print(f"Temperature: {celsius_temp:.2f}")
