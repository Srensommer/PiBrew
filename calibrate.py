import serial
import time


ser = serial.Serial('/dev/serial0', 115200)
command = 'rt14'.encode()
ser.write(command)
while not ser.in_waiting:  # Or: while self.ser.inWaiting():
	time.sleep(10)
print(ser.readline().decode())
