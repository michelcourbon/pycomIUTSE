from VZ89TE import VZ89TE
import utime
from machine import Pin, I2C

sensori2c = I2C(0,I2C.MASTER, pins=('P10','P11'), baudrate=10000)
sensor = VZ89TE(sensori2c)

print("I2C VZ89TE found at adr ", hex(sensori2c.scan()[0]) )
print("Revision: ", sensor.getRevision())
print("Year: ", sensor.getRevision()["Year"])
print("Month: ", sensor.getRevision()["Month"])
print("Day: ", sensor.getRevision()["Day"])

while True:
    try:
        co2 = sensor.getData()["CO2"]
    except ValueError: 
        co2 = co2
    
    try:
         print(sensor.getData())
    except ValueError:
         print("oops! crc error!")

    utime.sleep(3)
