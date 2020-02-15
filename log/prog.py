import time
import sys
from log.getValues import GetValues
import requests

mega = GetValues()
mega.clear_serial_read()

while True:
    water_temp = mega.get_water_temp()
#   beer_ph = mega.get_ph()
    tds = mega.get_tds()
    url = 'https://hansenbrew.dk/aquarium/postautolog'
    my_data = {"temp": 30, "ph": 0, "TDS": 888}

    x = requests.post(url, data=my_data)

    print(x.text)


