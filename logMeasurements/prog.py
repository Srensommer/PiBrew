debug = True
post_to_server = False

import time
import sys
if not debug:
    from getValues import GetValues
from dose_fertilizer import TimeChecker
import requests
from threading import Timer
import datetime

if not debug:
    mega = GetValues()
    mega.clear_serial_read()

time_checker = TimeChecker()


dose_time = datetime.time(hour=21, minute=9, second=0)
time_checker.init(dose_time)

while True:
    temp = 29
    ph = 8
    tds = 444

    if not debug:
        temp = mega.get_water_temp()
        ph = mega.get_ph()
        tds = mega.get_tds()
    url = 'https://hansenbrew.dk/aquarium/postautolog/'
    my_data = {"temp": temp, "ph": ph, "TDS": tds}
    
    if post_to_server:
        print("Making Request")
        x = requests.post(url, data=my_data)
        print("responsecode: " + x.status_code)
        if 200 <= x.status_code < 300:
            pass #log to file
    time.sleep(60*10)
