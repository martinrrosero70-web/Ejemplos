from machine import ADC, Pin
import time
POT_PIN = 36
pot = Pin(POT_PIN)
adc_pot = ADC (pot)
adc_pot .width(ADC.WIDTH_12BIT)
adc_pot . atten(ADC.ATTN_11DB)

while True:
    valor_pot = adc_pot.read()
    print(f"Valor POT : {valor_pot}")
    time.sleep(0.1)