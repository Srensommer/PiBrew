import serial
from shared.util.util import timestamp_print

#TODO: to kald til megaen går måske galt pt. håndter flere kald på en gang. "Hvad nu hvis klokken 13 sker på samme tidspunkt som hvert 10. minut?"

class MegaApi:
    def __init__(self):
        for serialcall in ['/dev/ttyUSB0', '/dev/serial0']:
            try:
                self.ser = serial.Serial(serialcall, 115200, timeout=10)
                if self.do_you_answer() == 50:
                    pass
                else:
                    # TODO prøv den næste
                    pass
            except:
                pass
        try:
            getattr(self, "ser")
        except:
            raise
            #TODO throw a meaningful error that crashes the program, as it is not meaningful to continue without a ser

    def write_to_mega(self, string):
        self.clear_serial_read()
        command = string.encode()
        self.ser.write(command)
        return self.ser.readline().decode()

    def do_you_answer(self):
        self.write_to_mega("test")

    def clear_serial_read(self):
        timestamp_print("Flush")
        self.ser.reset_input_buffer()

    def get_water_temp(self):
        self.clear_serial_read()
        command = 'wt'.encode()
        self.ser.write(command)
        return self.ser.readline().decode()

    def get_internal_temp(self):
        self.clear_serial_read()
        command = 'ait'.encode()
        self.ser.write(command)
        return self.ser.readline().decode()

    def get_internal_pressure(self):
        self.clear_serial_read()
        command = 'aip'.encode()
        self.ser.write(command)
        return self.ser.readline().decode()

    def get_external_temp(self):
        self.clear_serial_read()
        command = 'aet'.encode()
        self.ser.write(command)
        return self.ser.readline().decode()

    def get_external_pressure(self):
        self.clear_serial_read()
        command = 'aep'.encode()
        self.ser.write(command)
        return self.ser.readline().decode()

    def get_calibrate(self):
        self.clear_serial_read()
        command = 'c'.encode()
        self.ser.write(command)
        return self.ser.readline().decode()

    def get_sol_releases(self):
        self.clear_serial_read()
        command = 'sr'.encode()
        self.ser.write(command)
        return self.ser.readline().decode()

    def sol_open(self):
        self.clear_serial_read()
        command = 'so'.encode()
        self.ser.write(command)
        return self.ser.readline().decode()

    def sol_close(self):
        self.clear_serial_read()
        command = 'sc'.encode()
        self.ser.write(command)
        return self.ser.readline().decode()

    def sol_timed(self, time):
        self.clear_serial_read()
        command = 'sr' + str(time)
        command.encode()
        self.ser.write(command)
        return self.ser.readline().decode()

    def sol_clear_releases(self):
        self.clear_serial_read()
        command = 'sl'.encode()
        self.ser.write(command)
        return self.ser.readline().decode()

    def set_pressure_delta(self, delta):
        self.clear_serial_read()
        command = 'ad' + str(delta)
        self.ser.write(command.encode())
        return self.ser.readline().decode()
    
    def relay_open(self, relay_number):
        self.clear_serial_read()
        command = 'ro' + str(relay_number)
        self.ser.write(command.encode())
        return self.ser.readline().decode()

    def relay_close(self, relay_number):
        self.clear_serial_read()
        command = 'rc' + str(relay_number)
        self.ser.write(command.encode())
        return self.ser.readline().decode()

    def relay_timed(self, relay_number, time):
        self.clear_serial_read()
        command = 'rt' + str(relay_number) + str(time)
        self.ser.write(command.encode())
        return self.ser.readline().decode()

    def get_ph(self):
        self.clear_serial_read()
        command = 'p'.encode()
        self.ser.write(command)
        return self.ser.readline().decode()

    def get_tds(self):
        self.clear_serial_read()
        command = 't'.encode()
        self.ser.write(command)
        return self.ser.readline().decode()

