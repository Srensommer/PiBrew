import serial
import time
 
ser = serial.Serial('/dev/serial0', 115200)
command = 'rt011'.encode()
ser.write(command)
while not ser.in_waiting:  # Or: while self.ser.inWaiting():
    pass
print(ser.readline().decode())
