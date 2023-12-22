from machine import Pin 
#we are working on ESP32 so we need to import the Pin library from the machine library
import time
#we need to import the utime library for the delay function

pin = Pin("D13", Pin.OUT) # this is slightly different than Raspberry Pi Pico
pin.on()




         

