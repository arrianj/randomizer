from datetime import datetime
import requests, json
import pyinputplus as pyip

def date_num_generator():
    # get current microsecond value up to six decimal places
    current_time = datetime.now()
    x = current_time.microsecond 
    if x != 0:
        return (x)
    else:
        return 654321

def temp_num_generator():
    current_time = datetime.now()
    key_file = open('key.txt', 'r')
    api_key = key_file.readline().rstrip()
    key_file.close()
    # get temp in farenheit for rapid city, south dakota
    base_url = 'http://api.openweathermap.org/data/2.5/weather?id=5768233&appid='
    complete_url = base_url + api_key + '&units=imperial'
    response = requests.get(complete_url) 
    api = response.json()
    x = api['main']['temp']
    # run x through if statements to ensure seed can generate a high digit count number
    if x < 0:
        return  -x
    elif x == 0 or x == 1:
        return current_time.date 
    else:
        return x

def wind_num_generator():
    current_time = datetime.now()
    key_file = open('key.txt', 'r')
    api_key = key_file.readline().rstrip()
    key_file.close()
    # get wind speed in mph for buffalo, new york
    base_url = 'http://api.openweathermap.org/data/2.5/weather?id=5110629&appid='
    complete_url = base_url + api_key + '&units=imperial'
    response = requests.get(complete_url) 
    api = response.json()
    x = api['wind']['speed']
    # run x through if statements to ensure seed can generate a high digit count number
    if x < 0:
        return  -x * 99999
    elif x == 0 or x == 1:
        return current_time.date * 99999
    else:
        return x * 99999

def generator():
    date_num = date_num_generator()
    temp_num = temp_num_generator()
    wind_num = wind_num_generator()
    # create new numbers by performing some equations on the values generated by the openweather API and from the current time  
    raw_num_1 = date_num * round(temp_num * date_num) * round(wind_num * date_num) * round(date_num * wind_num ** temp_num)
    raw_num_2 = date_num * round(temp_num * date_num) * round(wind_num * temp_num) * round(date_num * wind_num ** temp_num)
    raw_num_3 = date_num * round(temp_num * wind_num) * round(wind_num * date_num) * round(date_num * wind_num ** temp_num)
    raw_num_4 = round(date_num * wind_num) * round(wind_num * date_num) * round(temp_num * wind_num ** temp_num)
    raw_num_5 = round(wind_num ** temp_num) * round(temp_num * wind_num ** temp_num)
    # combine those new numbers into a single string
    full_num = str(raw_num_1) + str(raw_num_2) + str(raw_num_3) + str(raw_num_4) + str(raw_num_5)
    return full_num

def num_picker():
    full_num = generator()
    # variable to set length of final number
    # make option to set to max?
    range_choice = pyip.inputNum(max=len(full_num), prompt=(f'[?] How many digits do you want to generate? (Enter 0 for the maximum of {len(full_num)}): '))
    if range_choice == 0:
        range_choice = len(full_num)
    # flag to enable formatting for the final number
    format_num = pyip.inputYesNo(prompt=('[?] Do you want to use decimal separators? (e.g. The commas in: 1,234,567,890) [Y/N]: '))
    if format_num == 'yes':
        formatted_num = f'{int(full_num[0:range_choice]):,}'
        print(formatted_num)
    else:
        print(full_num[0:range_choice])