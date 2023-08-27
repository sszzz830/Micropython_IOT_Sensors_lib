from utime import sleep_ms

PWR_OFF = 0x00
PWR_ON = 0x01
RESET = 0x07
CONT_LOWRES = 0x13
CONT_HIRES_1 = 0x10
CONT_HIRES_2 = 0x11
ONCE_HIRES_1 = 0x20
ONCE_HIRES_2 = 0x21
ONCE_LOWRES = 0x23

class BH1750():
    def __init__(self, bus, addr=0x23):
        self.bus = bus
        self.addr = addr
        self.off()
        self.reset()
    def off(self):
        self.set_mode(PWR_OFF)
    def on(self):
        self.set_mode(PWR_ON)
    def reset(self):
        self.on()
        self.set_mode(RESET)
    def set_mode(self, mode):
        self.mode = mode
        self.bus.writeto(self.addr, bytes([self.mode]))
    def luminance(self, mode):
        if mode & 0x10 and mode != self.mode:
            self.set_mode(mode)
        if mode & 0x20:
            self.set_mode(mode)
        sleep_ms(24 if mode in (CONT_LOWRES, ONCE_LOWRES) else 180)
        data = self.bus.readfrom(self.addr, 2)
        factor = 2.0 if mode in (CONT_HIRES_2, ONCE_HIRES_2) else 1.0
        return (data[0]<<8 | data[1]) / (1.2 * factor)