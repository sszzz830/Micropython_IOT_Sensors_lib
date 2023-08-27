from machine import ADC

class CSMS2:
    def __init__(self, pin):
        self.adc = ADC(pin)
        self.adc.atten(ADC.ATTN_11DB)

    def measure(self):
        raw_value = self.adc.read()
        processed_value = 100-(raw_value - 1050)//20
        if processed_value < 0:
            return 0
        elif processed_value > 100:
            return 100
        else:
            return processed_value

    