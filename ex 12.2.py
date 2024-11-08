import requests
import json
city_name=input("Enter city name: ")
api_key= "f540fba3af1f42b63f4f4669d3d52443"
url=f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
response = requests.get(url)
#print(json.dumps(response.json(),indent=2))
for data in response.json()['weather']:
    print("Weather: " + data['main'])
    print("Description " + data['description'])
print(f"Temperature : {response.json()['main']['temp']}\u00B0C")
