from machine import I2C
import time
from ADS1115 import ADS1115

# initialize the I2C bus 
i2c = I2C(0)                         # create on bus 0
i2c = I2C(0, I2C.MASTER)             # create and init as a master
i2c = I2C(0, pins=('P9','P10'))      # PIN assignments (P9=SDA, P10=SCL)
i2c.init(I2C.MASTER, baudrate=10000) # init as a master

# Setup ADS1115 using defaults (0x48 address and 4.096V max range)
#i2c = I2C(0, I2C.MASTER)
adc = ADS1115(i2c)

# pycom.heartbeat(False)

# Read the ADC on a 5 second interval
while True :
    print("\nChannel 0 voltage: {} V".format(adc.get_voltage(0)))
    print("Channel 0 ADC value: {} \n".format(adc.read(0)))
    time.sleep(5)
