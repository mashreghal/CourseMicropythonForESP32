#we are using the ADC1 channel 0 of ESP32 which is pin number 36.
#The ADC1 has 12 bit resolution so the output will be 0 to 4095 which corresponds to 0 to 1V
from machine import Pin, ADC
import time

analog_in = ADC(Pin(36)) 
analog_in.atten(ADC.ATTN_11DB) #Full range: 3.3v

while True:
    value = 1 * analog_in.read_u16() / 4095
    print(value)
    time.sleep(1)
    



         

