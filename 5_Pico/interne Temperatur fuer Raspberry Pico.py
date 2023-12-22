# read Raspberry Picos internal temperature sensor via micro python
from machine import ADC 
import utime


#create ADC object on ADC pin 4
ad_read = ADC(4)
#Yes, if you want to read from another channel, you would need to create another ADC object. Each ADC object is associated with a specific pin on the Raspberry Pico, and it allows you to read analog values from that pin. By creating a new ADC object and specifying a different pin number, you can read from a different channel.
#For example, if you want to read from channel 5, you can create a new ADC object like this:

# we will read the internal temperature sensor continuously
while True:
    # read the internal temperature sensor
    temp_value = ad_read.read_u16() # read the ADC value, which is a 16-bit integer
    # the maximum value of the ADC is 65535, which corresponds to 3.3V
    temp_resolution = 3.3 / 65535 # convert ADC value to voltage
    temp_voltage = temp_value * temp_resolution # convert ADC value to voltage
    # from the controllers datasheet we know the following:
    # Bei 27°C beträgt die Spannung 0,706 V und eine Änderung von 1°C entspricht 1.721mV
    #According to the datasheet, the voltage decreases as the temperature increases. At 27°C, the voltage is 0.706V, and for every increase of 1°C, the voltage decreases by 1.721mV
    temperature= 27 - (temp_voltage - 0.706) /0.001721
    print("Temperature on the chip: ", temperature, "°C")
    utime.sleep(1) # wait 1 second before reading again