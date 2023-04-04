import datetime as dt
import requests 


BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
API_KEY = open('usingPython\credentials.txt', 'r').read()
CITY = input("Enter the city")

# print(API_KEY)

def kelvin_to_celsius_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius *(9/5)+32
    return celsius,fahrenheit

url = BASE_URL +"appid="+ API_KEY + "&q=" + CITY 

response = requests.get(url).json()

# print(response)
# print(response['main']['temp'])

temp_kelvin = response['main']['temp']
temp_celsius, temp_fahrenheit = kelvin_to_celsius_fahrenheit(temp_kelvin)
feels_like_kelvin = response['main']['feels_like']
feels_like_celsius, feels_like_fahrenheit = kelvin_to_celsius_fahrenheit(feels_like_kelvin)
humidity = response['main']['humidity']
description = response['weather'][0]['description']
sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])
wind = response['wind']['speed']

print(f"Temperature in {CITY}: {temp_celsius:.2f}C or {temp_fahrenheit}F")
print(f"Temperature in {CITY} feels like: {feels_like_celsius:.2f}C or {feels_like_fahrenheit}F")
print(f"Humidity in {CITY}: {humidity}%")
print(f"Wind Speed in {CITY}: {wind}km/h")
print(f"General Weather in {CITY}: {description}")
print(f"Sunrises in {CITY}: {sunrise_time} local time")
print(f"Sunsets in {CITY}: {sunset_time} local time")
