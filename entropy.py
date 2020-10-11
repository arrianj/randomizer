from datetime import datetime
import requests, json
import config

def date_gen():
    # get current microsecond value up to six decimal places
    current_time = datetime.now()
    x = current_time.microsecond 
    if x != 0:
        return (x)

def temp_gen():
    api_key = config.api_key
    # get temp in farenheit for rapid city, south dakota
    base_url = 'http://api.openweathermap.org/data/2.5/weather?id=5768233&appid='
    complete_url = base_url + api_key + '&units=imperial'
    response = requests.get(complete_url) 
    api = response.json()
    x = api['main']['temp']
    return x

def generator():
    date_num = date_gen()
    temp_num = temp_gen()
    full_number = str(date_num) + str(temp_num)
    print(full_number)
