from machine import Pin, PWM
# go to micropython website and check documentation for the ESP32
#we are working on ESP32 so we need to import the Pin library from the machine library

pwm1 =PWM(Pin(16),freq=1,duty=512) # 1Hz and 50% duty cycle

while True:
    pass
# schaue dir die Demo von Werner an mit seiner LED





         

