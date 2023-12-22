# This script will be executed by the Python interpreter and make the LED of the Raspberry Pi Oico blink.
from machine import Pin
import utime

onboard_led = Pin(25, Pin.OUT) # create a Pin object for the onboard LED

for i in range(10): # loop 10 times
    onboard_led.toggle() # turn the LED on
    utime.sleep(0.5) # wait for 0.5 seconds
    onboard_led.toggle() # turn the LED off
    utime.sleep(0.5) # wait for 0.5 seconds