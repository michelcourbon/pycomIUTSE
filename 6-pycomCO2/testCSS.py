from machine import I2C
import time
import CCS811

i2c = I2C(0,I2C.MASTER, pins=('P10','P11'), baudrate=10000)

ccs = CCS811.CCS811(i2c=i2c,addr=90)
print('wait component ready and after every 3 seconds')
time.sleep(2)

while True:
    ccs.data_ready()
    time.sleep(3)
    co2 = ccs.eCO2
    voc = ccs.tVOC
    if co2 > 10:
        print('CO2 level: ' + str(co2) + ' ppm & tVOC level: ' + str(voc))
