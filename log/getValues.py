import serial


class GetValues:
    ser = serial.Serial('/dev/serial0', 115200, timeout=4)

    def clear_serial_read(self):
        while self.ser.in_waiting:  # Or: while self.ser.inWaiting():
            print(self.ser.readline())

    def get_water_temp(self):
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

    def relay_open(self, relay_number):
        command = 'ro' + relay_number
        self.ser.write(command.encode())
        return self.ser.readline().decode()

    def relay_close(self, relay_number):
        command = 'rc' + relay_number
        self.ser.write(command.encode())
        return self.ser.readline().decode()

    def relay_timed(self, relay_number, time):
        command = 'rt' + relay_number + time
        self.ser.write(command.encode())
        return self.ser.readline().decode()

    def get_ph(self):
        command = 'p'.encode()
        self.ser.write(command)
        return self.ser.readline().decode()

    def get_tds(self):
        command = 't'.encode()
        self.ser.write(command)
        return self.ser.readline().decode()
