import serial


class GetValues:
    ser = serial.Serial('/dev/ttyACM0', 115200, timeout=4)

    def clear_serial_read(self):
        while self.ser.in_waiting:  # Or: while self.ser.inWaiting():
            print(self.ser.readline())

    def get_beer_temp(self):
        command = 'wt'.encode()
        self.ser.write(command)
        return self.ser.readline().decode()

    def get_internal_temp(self):
        command = 'ait'.encode()
        self.ser.write(command)
        return self.ser.readline().decode()

    def get_internal_pressure(self):
        command = 'aip'.encode()
        self.ser.write(command)
        return self.ser.readline().decode()

    def get_external_temp(self):
        command = 'aet'.encode()
        self.ser.write(command)
        return self.ser.readline().decode()

    def get_external_pressure(self):
        command = 'aep'.encode()
        self.ser.write(command)
        return self.ser.readline().decode()

    def get_calibrate(self):
        command = 'c'.encode()
        self.ser.write(command)
        return self.ser.readline().decode()

    def get_sol_releases(self):
        command = 'sr'.encode()
        self.ser.write(command)
        return self.ser.readline().decode()

    def sol_open(self):
        command = 'so'.encode()
        self.ser.write(command)
        return self.ser.readline().decode()

    def sol_close(self):
        command = 'sc'.encode()
        self.ser.write(command)
        return self.ser.readline().decode()

    def sol_timed(self, time):
        command = 'sr' + time
        command.encode()
        self.ser.write(command)
        return self.ser.readline().decode()

    def sol_clear_releases(self):
        command = 'sl'.encode()
        self.ser.write(command)
        return self.ser.readline().decode()

    def relay_open(self):
        command = 'ro'.encode()
        self.ser.write(command)
        return self.ser.readline().decode()

    def relay_close(self):
        command = 'rc'.encode()
        self.ser.write(command)
        return self.ser.readline().decode()

    def relay_timed(self, time):
        command = 'rt' + time
        command.encode()
        self.ser.write(command)
        return self.ser.readline().decode()

    def get_beer_ph(self):
        command = 'p'.encode()
        self.ser.write(command)
        return self.ser.readline().decode()
