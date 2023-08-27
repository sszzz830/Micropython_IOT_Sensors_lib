from machine import UART
import utime

class JW01:
    BAUDRATE = 9600
    BITS = 8
    PARITY = None
    STOP = 1
    ADDR = 0x2C
    FULL_SCALE_HIGH = 0x03
    FULL_SCALE_LOW = 0xFF
    def __init__(self,uart):
        self.uart = uart
    def _checksum(self, data):
        return sum(data[:-1]) & 0xFF
    def verify_checksum(self, data):
        return data[-1] == self._checksum(data)
    def measure(self):
        while True:
            data=self.uart.read()
            if data and len(data) >= 6 and data[0] == self.ADDR and self.verify_checksum(data):
                CO2_high, CO2_low = data[1], data[2]
                return CO2_high*256 + CO2_low
            else:
                utime.sleep_ms(100)
