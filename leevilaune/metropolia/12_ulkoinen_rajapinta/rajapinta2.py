import json
import requests

def get_coordinates(city,apikey):
    geolocation_request = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid={apikey}"
    city_response = requests.get(geolocation_request).json()[0]
    return {"lon":city_response["lon"],"lat":city_response["lat"]}

def get_weather(city, apikey):
    city_loc = get_coordinates(city, apikey)
    lon = city_loc["lon"]
    lat = city_loc["lat"]
    weather_request = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={apikey}&units=metric"
    return requests.get(weather_request).json()

with open("../../../weatherapi.json") as file:
    apikey = json.load(file)["apikey"]

while True:
    city = input("Anna kaupunki: ")
    if city == "":
        break
    weather = get_weather(city, apikey)
    w_desc = weather["weather"][0]["description"]
    w_celsius = weather["main"]["temp"]
    print(f"Kuvaus: {w_desc}, Lämpotila: {w_celsius}C")