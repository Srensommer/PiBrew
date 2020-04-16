debug = False
post_to_server = True

if not debug:
    from megaApi import MegaApi
from dose_fertilizer import TimeChecker
import requests
from threading import Timer
from datetime import datetime, timedelta, time
import time as delay


def post_log_to_server(temp, ph, tds):
    url = 'https://hansenbrew.dk/aquarium/postautolog/'
    my_data = {"temp": temp, "ph": ph, "TDS": tds}

    if post_to_server:
        posted = False
        while not posted:
            print("Making Request")
            try:
                x = requests.post(url, data=my_data, timeout=10)
                print("responsecode: " + str(x.status_code))
                posted = True
                if 200 <= x.status_code < 300:
                    return True
                return False

            except requests.exceptions.Timeout:
                print("Post to server - timeout")
            except requests.exceptions.RequestException as e:
                print("Post to server - ConnectionError", e)

    return True


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
        temp = 30
        ph = 0
        tds = 0

        posted = False
        while not posted:
            if not debug:
                temp = self.mega.get_water_temp()
                ph = self.mega.get_ph()
                tds = self.mega.get_tds()
                print("temp: " + str(temp))
                print("tds: " + str(tds))
            posted = post_log_to_server(temp, ph, tds)
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


something = Program()
while True:
    delay.sleep(60*60*24)
