from datetime import datetime

def date_gen():
    current_time = datetime.now()
    x = current_time.microsecond 
    print(x)

