from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import time
from os import system

system("cls")

class Weather:
    def __init__(self):
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_argument("disable-extensions")
        self.browserProfile.add_argument("disable-gpu")
        self.browserProfile.add_argument("headless")
        self.browserProfile.add_argument("no-sandbox")
        self.browserProfile.add_experimental_option("prefs",{"intl.accept_languages":"en"})
        self.browser = webdriver.Chrome("chromedriver.exe",chrome_options=self.browserProfile)
        self.browser.get("https://yandex.com/weather/")
    def City_search(self,search):
        search_button = self.browser.find_element_by_id("header2input")
        search_button.send_keys(search)
        time.sleep(2)
        search_button2 = self.browser.find_element_by_xpath('//*[@id="search-results"]/li[1]/a')
        search_button2.click()
        url = self.browser.current_url
        self.browser.close()
        html = requests.get(url).content
        soup = BeautifulSoup(html,"html.parser")
        tempt = soup.find("div",{"class":"temp fact__temp fact__temp_size_s"}).find("span",{"class":"temp__value"}).text
        status = soup.find("div",{"class":"link__condition day-anchor i-bem"}).text
        rain_humidity = soup.find("div",{"class":"term term_orient_v fact__humidity"}).text
        weather_in = soup.find("div",{"class":"header-title header-title_in-fact"}).find("h1").text
        system("cls")
        print(weather_in)
        print(status)
        print(f"Degrees {tempt}° \nRain Humidty {rain_humidity}")

system("cls")
print("Enter a city") 
city = input(">")

w1 = Weather()
w1.City_search(city)

