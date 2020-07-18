import serial
import time


ser = serial.Serial('/dev/ttyUSB0', 115200)
command = 'aep'.encode()
time.sleep(2)
while True:
    ser.write(command)
    while not ser.in_waiting:  # Or: while self.ser.inWaiting():
        time.sleep(10)
    print(ser.readline().decode())
