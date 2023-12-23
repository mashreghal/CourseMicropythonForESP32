from pyb import DAC 
import math

buf = bytearray(100)
for i in range(len(buf)):
    buf[i] = 128 + int(127 * math.sin(2 * math.pi * i / len(buf)))
"""    
The reason for the shift of 128 is not related to the range of i, but rather to the range of values that the math.sin function can return. 
The math.sin function returns values in the range -1 to 1. When this is multiplied by 127, the result is a value in the range -127 to 127.
The shift of 128 is used to ensure that all values are positive before they are stored in the bytearray buf. 
This is because bytearrays in Python can only store positive integers. By adding 128 to the result, the range of possible values becomes 1 to 255, which are all valid values for a bytearray.
"""
dac = DAC(1)
dac.write_timed(buf, 400 * len(buf), mode=DAC.CIRCULAR) # 400 * len(buf) = 40000
 

         

