# siehe dir das Video an, das ganze war f�r ESP32 nicht leicht verf�gbar.
# es gibt ein schematic wo alle eingezeichnet, schaue dir unbedingt das Video an
from multiprocessing import popen_spawn_win32
from machine import DAC, Pin 

dac = DAC(Pin(26))
dac.write(128) # 0-255 255 entsprechen 3.3 Volt




         

