from dose_fertilizer import TimeChecker
from util import time_stamp_print
from apiCalls import ApiCalls
from threading import Timer
from datetime import datetime, timedelta, time
import time as delay

debug = False

if not debug:
    from megaApi import MegaApi


class Program:
    if not debug:
        mega = MegaApi()
        mega.clear_serial_read()

    def __init__(self):
        time_stamp_print("Init")
        self.measure()

    def measure(self):
        data = {
            "beer_temp": 0,
            "beer_ph": 0,
            "internal_temp": 0,
            "external_temp": 0,
            "internal_pressure": 0,
            "external_pressure": 0,
            "air_releases_since_last_log": 0
        }

        posted = False
        while not posted:
            if not debug:
                data = {
                    "beer_temp": self.mega.get_water_temp(),
                    "beer_ph": 0,
                    "internal_temp": self.mega.get_internal_temp(),
                    "external_temp": self.mega.get_external_temp(),
                    "internal_pressure": self.mega.get_internal_pressure(),
                    "external_pressure": self.mega.get_external_pressure(),
                    "air_releases_since_last_log": self.mega.get_sol_releases()
                }
                time_stamp_print(str(data))
            if not debug: 
                self.mega.sol_clear_releases()
                self.mega.set_pressure_delta(20)
            posted = ApiCalls('brewbotics/upload/new/measurement/').post_log_to_server(data)
        self.measure_timer()

    def measure_timer(self):
        now = datetime.today()
        next_measure_time = now + timedelta(minutes=10 - (now.minute % 10)) - timedelta(seconds=now.second)

        secs = (next_measure_time - now).total_seconds()
        time_stamp_print("Next measure in:  " + str(int(secs / 60)) + "min and " + str(secs % 60) + "secs")

        t = Timer(secs, self.measure)
        t.start()


something = Program()
while True:
    delay.sleep(60 * 60 * 24)
