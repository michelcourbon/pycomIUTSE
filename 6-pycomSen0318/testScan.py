
# default P9 = SDA = green / P10 = SCL = blue
# verify CC811 chip 

from machine import I2C

i2c = I2C(0, I2C.MASTER, baudrate=100000) 
i2c.init(I2C.MASTER)
i2c.scan()  
