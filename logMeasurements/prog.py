import time
import sys
#from getValues import GetValues
from dose_fertilizer import TimeChecker
import requests
from threading import Timer
import datetime



#mega = GetValues()
#mega.clear_serial_read()

time_checker = TimeChecker()


dose_time = datetime.time(hour=18, minute=8, second=0)
time_checker.init(dose_time)

while True:
    print("new termination")
    #water_temp = mega.get_water_temp()
#   beer_ph = mega.get_ph()
#   tds = mega.get_tds()
    url = 'https://hansenbrew.dk/aquarium/postautolog/'
    my_data = {"temp": 30, "ph": 0, "TDS": 888}

    

    print("Making Request")
    x = requests.post(url, data=my_data)
    print("Response:")
    print(x.status_code)
    if (x.status_code >= 200 and x.status_code < 300):
        pass #log to file
    time.sleep(60*10)
