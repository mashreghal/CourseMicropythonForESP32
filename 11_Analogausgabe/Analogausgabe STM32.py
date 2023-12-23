from pyb import DAC, Pin #beim ESP32 war es anders

dac = DAC(Pin('PA4'))
dac.write(0) # 0-4095 4095 entsprechen 3.3 Volt da 12bit

         

