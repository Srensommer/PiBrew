import time
import sys
from getValues import GetValues
from dose_fertilizer import TimeChecker
import requests

mega = GetValues()
mega.clear_serial_read()

time_checker = TimeChecker()

while True:
    water_temp = mega.get_water_temp()
#   beer_ph = mega.get_ph()
    tds = mega.get_tds()
    url = 'https://hansenbrew.dk/aquarium/postautolog'
    my_data = {"temp": 30, "ph": 0, "TDS": 888}

    if time_checker.should_fertilize():
        mega.relay_timed(1, 4)

    x = requests.post(url, data=my_data)

    print(x.text)
    time.sleep(60*10)


