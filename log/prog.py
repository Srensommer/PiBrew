import serial
import time
import sys

ser = serial.Serial('/dev/ttyACM0',115200)
while True:
    command = 'st2'.encode()
    ser.write(command)
    time.sleep(8)
    print(ser.readline().decode())
while (True):
    pass
