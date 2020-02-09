import time
import sys
from . import getValues

mega = getValues.GetValues
while True:
    beer_temp = mega.get_beer_temp()
    internal_temp = mega.get_internal_temp()
    internal_pressure = mega.get_internal_pressure()
    external_temp = mega.get_external_temp()
    external_pressure = mega.get_external_pressure()
    beer_ph = mega.get_beer_ph()





    command = 'st2'.encode()
    self.ser.write(command)
    time.sleep(8)
    print(ser.readline().decode())


