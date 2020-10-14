from datetime import datetime
import requests, json
import pyinputplus as pyip

def date_num_generator():
    # get current microsecond value up to six decimal places
    current_time = datetime.now()
    x = current_time.microsecond 
    if x != 0:
        return (x)

def temp_num_generator():
    key_file = open('key.txt', 'r')
    api_key = key_file.readline().rstrip()
    key_file.close()
    # get temp in farenheit for rapid city, south dakota
    base_url = 'http://api.openweathermap.org/data/2.5/weather?id=5768233&appid='
    complete_url = base_url + api_key + '&units=imperial'
    response = requests.get(complete_url) 
    api = response.json()
    x = api['main']['temp']
    return x

def wind_num_generator():
    key_file = open('key.txt', 'r')
    api_key = key_file.readline().rstrip()
    key_file.close()
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
    raw_num_1 = str(date_num * int(temp_num * date_num) * int(wind_num * date_num) * int(date_num * wind_num ** temp_num))
    raw_num_2 = str(date_num * int(temp_num * date_num) * int(wind_num * temp_num) * int(date_num * wind_num ** temp_num))
    raw_num_3 = str(date_num * int(temp_num * wind_num) * int(wind_num * date_num) * int(date_num * wind_num ** temp_num))
    full_num = raw_num_1 + raw_num_2 + raw_num_3
    return full_num

def num_picker():
    full_num = generator()
    format_num = pyip.inputYesNo(prompt=('[?] Do you want to use decimal separators? (e.g. 1,234,567,890) [Y/N]: '))
    if format_num == 'yes':
        full_num_formatted = f'{int(full_num):,}'
        print(full_num_formatted)
    else:
        print(full_num)