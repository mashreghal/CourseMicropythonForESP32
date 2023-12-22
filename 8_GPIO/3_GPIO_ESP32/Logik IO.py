from machine import Pin, Signal
from time import sleep

my_pin = Pin(17, Pin.OUT)
my_signal = Signal(my_pin, invert=True)

while True:
    my_pin.on() # LED an
    my_signal.on() # LED waere aus da invertiert
    
# mit signals koennen wir generischer arbeiten, da wir nicht wissen, ob wir invertieren muessen