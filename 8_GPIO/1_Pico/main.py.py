from machine import Pin 
#we are wroking on a raspberry pi pico so we need to import the pin library
import time
#we need to import the utime library for the delay function

while True:
    led_gruen = Pin(2,Pin.OUT) #instatiate an instance of the pin class called led_gruen
    led_gruen.on() #turn the led on
    time.sleep(1) #wait for 1 second
    led_gruen.off() #turn the led off
    time.sleep(1) #wait for 1 second


         

