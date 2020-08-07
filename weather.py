import requests
import json
from os import system




system("cls")
api_key = ""


class WeatherForecast():
    def __init__(self,city,api_key):
        self.city = city
        self.api_key = api_key
        self.total_url = f"http://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={self.api_key}&units=metric"
        self.result = requests.get(self.total_url)
        self.result= json.loads(self.result.text)
    def WeatherResult(self):
        self.city_name = self.result["name"]
        self.tempt = self.result["main"]["temp"]
        self.status = self.result["weather"][0]["description"]
        self.humidity = self.result["main"]["humidity"]
        correction = "Province" in self.city_name
        if correction == True:
            corrected_city=self.city_name.replace("Province","")
            print(corrected_city)
        elif correction == False:
            print(self.city_name)
        print(str(self.status).capitalize())
        print(f"Degrees {self.tempt}° \ Humidty %{self.humidity}")
        
print("Enter a city name")
city_name = input(">")        
system("cls")

try:
    w1 = WeatherForecast(city_name,api_key)
    w1.WeatherResult()
except KeyError:
    print(f"No city named {city_name}")
