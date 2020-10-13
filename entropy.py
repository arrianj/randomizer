from datetime import datetime
import requests, json
import config

def date_num_generator():
    # get current microsecond value up to six decimal places
    current_time = datetime.now()
    x = current_time.microsecond 
    if x != 0:
        return (x)

def temp_num_generator():
    api_key = config.api_key
    # get temp in farenheit for rapid city, south dakota
    base_url = 'http://api.openweathermap.org/data/2.5/weather?id=5768233&appid='
    complete_url = base_url + api_key + '&units=imperial'
    response = requests.get(complete_url) 
    api = response.json()
    x = api['main']['temp']
    return x

def wind_num_generator():
    api_key = config.api_key
    # get wind speed in mph for buffalo, new york
    base_url = 'http://api.openweathermap.org/data/2.5/weather?id=5110629&appid='
    complete_url = base_url + api_key + '&units=imperial'
    response = requests.get(complete_url) 
    api = response.json()
    x = api['wind']['speed']
    return x

def generator():
    date_num = date_num_generator()
    temp_num = temp_num_generator()
    wind_num = wind_num_generator()
    full_number = date_num * int(temp_num * date_num) * int(wind_num * date_num)
    print(full_number)
