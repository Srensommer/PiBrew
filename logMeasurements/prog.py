debug = False
post_to_server = True

if not debug:
    from megaApi import MegaApi
from dose_fertilizer import TimeChecker
import requests
from requests.exceptions import Timeout
from threading import Timer
from datetime import datetime, timedelta, time
import time as delay


class Program:
    dose_time = time(hour=13, minute=00, second=0)

    if not debug:
        mega = MegaApi()
        mega.clear_serial_read()
        time_checker = TimeChecker(dose_time)
        time_checker.dosing_version(dose_time, mega)
    else:
        time_checker = TimeChecker(dose_time)

    def __init__(self):
        print("Init")
        self.measure()

    def measure(self):
        temp = 29
        ph = 8
        tds = 444

        if not debug:
            temp = self.mega.get_water_temp()
            #  ph = mega.get_ph()
            tds = self.mega.get_tds(temp)
            print(temp)
        url = 'https://hansenbrew.dk/aquarium/postautolog/'
        my_data = {"temp": temp, "ph": ph, "TDS": tds}

        if post_to_server:
            posted = False
            while not posted:
                print("Making Request")
                try:
                    x = requests.post(url, data=my_data, timeout=10)
                    print("responsecode: " + str(x.status_code))
                    if 200 <= x.status_code < 300:
                        posted = True
                        pass #log to file
                except Timeout:
                    print("try to post again")

        self.measure_timer()

    def measure_timer(self):
        now = datetime.today()
        next_measure_time = now + timedelta(
            minutes=10 - now.minute % 10,
            seconds=10 - now.second % 10,
            microseconds=0
        )

        secs = (next_measure_time - now).total_seconds()
        print("Next measure in:  " + str(secs) + " seconds")

        t = Timer(secs, self.measure)
        t.start()


something = Program
while True:
    delay.sleep(60*60*24)