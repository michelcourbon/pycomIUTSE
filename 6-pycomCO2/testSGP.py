from machine import I2C
import time
import adafruit_sgp30

i2c = I2C(0,I2C.MASTER, pins=('P10','P11'), baudrate=10000)
sgp30 = adafruit_sgp30.Adafruit_SGP30(i2c)

print('wait 5s startup warming')
time.sleep(5)

while True:
    co2eq, tvoc = sgp30.iaq_measure()
    print("CO2eq = %d ppm \t TVOC = %d ppb" % (co2eq, tvoc))
    time.sleep(3)
