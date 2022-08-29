
# default P9 = SDA = green / P10 = SCL = blue
# verify CC811 chip at 90 / ADS1115 at 0x48 or 0x49 not working ?

from machine import I2C

i2c = I2C(0, I2C.MASTER, baudrate=100000) 
i2c.init(I2C.MASTER)
i2c.scan()  
