# wir bauen eine Ampelschaltung mit 3 LEDs am ESP32 mit Micropython
#Schaue das Kurzvideo wo die Schaltung gezeigt wird
import time
from machine import Pin

SW1 = 16 #switch 1
SW2 = 17
SW3 = 18

sw1 = Pin(SW1, Pin.IN,Pin.PUll_UP)
sw2 = Pin(SW2, Pin.IN,Pin.PUll_UP)
sw3 = Pin(SW3, Pin.IN,Pin.PUll_UP)


while True:
   print("SW1: ",sw1.value())
   print("SW2: ",sw2.value())
   print("SW3: ",sw3.value())
   print("-----")
   time.sleep(0.5)
   
    
    




         

