debug = False
post_to_server = True

import time
import sys
if not debug:
    from megaApi import MegaApi
from dose_fertilizer import TimeChecker
import requests
from threading import Timer
import datetime


dose_time = datetime.time(hour=13, minute=00, second=0)

if not debug:
    mega = MegaApi()
    mega.clear_serial_read()
    time_checker = TimeChecker(dose_time)
    time_checker.dosing_version(dose_time, mega)
else:
    time_checker = TimeChecker(dose_time)


while True:
    temp = 29
    ph = 8
    tds = 444

    if not debug:
        temp = mega.get_water_temp()
      #  ph = mega.get_ph()
      #  tds = mega.get_tds()
        print(temp)
    url = 'https://hansenbrew.dk/aquarium/postautolog/'
    my_data = {"temp": temp, "ph": ph, "TDS": tds}
    
    if post_to_server:
        print("Making Request")
        x = requests.post(url, data=my_data)
        print("responsecode: " + str(x.status_code))
        
        if 200 <= x.status_code < 300:
            pass #log to file
    time.sleep(60*10)
