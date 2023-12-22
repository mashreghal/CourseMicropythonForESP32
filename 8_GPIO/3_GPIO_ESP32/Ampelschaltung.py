# wir bauen eine Ampelschaltung mit 3 LEDs am ESP32 mit Micropython
import time
from machine import Pin

gruen = 16
gelb = 17
rot = 18

pin_gruen = Pin(gruen, Pin.OUT)
pin_gelb = Pin(gelb, Pin.OUT)
pin_rot = Pin(rot, Pin.OUT)

def AmpelGruen(dauer):
    pin_gruen.on()
    pin_gelb.off()
    pin_rot.off()
    time.sleep(dauer)
    
def AmpelGelb(dauer):
    pin_gruen.off()
    pin_gelb.on()
    pin_rot.off()
    time.sleep(dauer)
    
def AmpelRot(dauer):
    pin_gruen.off()
    pin_gelb.off()
    pin_rot.on()
    time.sleep(dauer)
    
def AmpelRotGelb(dauer):
    pin_gruen.off()
    pin_gelb.on()
    pin_rot.on()
    time.sleep(dauer)
while True:
   AmpelGruen(3)
   AmpelGelb(1)
   AmpelRot(5)
   AmpelRotGelb(1)
   
    
    




         

