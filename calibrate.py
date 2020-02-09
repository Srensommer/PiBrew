import serial
import time


ser = serial.Serial('/dev/ttyAMA0', 115200)
command = 'c'.encode()
ser.write(command)
while not ser.in_waiting:  # Or: while self.ser.inWaiting():
	time.sleep(1)
print(ser.readline().decode())
