from machine import I2C

i2c= I2C(0,I2C.MASTER, pins=('P10','P11'), baudrate=10000)
print(i2c.scan())
