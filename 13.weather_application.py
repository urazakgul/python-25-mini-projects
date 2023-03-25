# Bu proje, belirli bir konum için mevcut hava koşullarını ve tahminleri gösteren bir program oluşturmayı içerir.
# (This project involves creating a program that displays the current weather conditions and forecast for a specified location.)

# API Key: https://home.openweathermap.org/users/sign_up

import requests

api_key = input("Please enter your OpenWeatherMap API key: ")
city = input("Please enter a city: ")
city = city.capitalize()

url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
response = requests.get(url)
data = response.json()

temp_kelvin = data["main"]["temp"]
humidity = data["main"]["humidity"]
temp_celsius = temp_kelvin - 273.15
weather = data["weather"][0]["description"].capitalize()

print(f"Current weather in {city}: {weather}.")
print(f"Temperature: {temp_celsius:.1f} Celsius")
print(f"Humidity: {humidity}%.")

num_forecasts = int(input("How many weather forecasts would you like to see? "))

forecast_url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}"
forecast_response = requests.get(forecast_url)
forecast_data = forecast_response.json()

for i in range(num_forecasts):
    date = forecast_data["list"][i]["dt_txt"]
    forecast_temp_kelvin = forecast_data["list"][i]["main"]["temp"]
    forecast_temp_celsius = forecast_temp_kelvin - 273.15
    forecast_weather = forecast_data["list"][i]["weather"][0]["description"].capitalize()
    print(f"Date: {date}. Weather forecast: {forecast_weather}. Temperature forecast: {forecast_temp_celsius:.1f} Celsius")