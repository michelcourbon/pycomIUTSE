#!/usr/bin/env python
#
# Copyright (c) 2020, Pycom Limited.
#
# This software is licensed under the GNU GPL version 3 or any
# later version, with permitted additional terms. For more information
# see the Pycom Licence v1.0 document supplied with this file, or
# available at https://www.pycom.io/opensource/licensing
#

# See https://docs.pycom.io for more information regarding library specifics

import time
import pycom
from pysense import Pysense
import machine

from LIS2HH12 import LIS2HH12
from SI7006A20 import SI7006A20
from LTR329ALS01 import LTR329ALS01
from MPL3115A2 import MPL3115A2,ALTITUDE,PRESSURE

pycom.heartbeat(False)
pycom.rgbled(0x0A0A08) # white

py = Pysense()

# run number..
num = 0

while True:

    print("==================================================================================")
    pycom.rgbled(0x007f00) # switch to green color for embedded led

    print("run number = "+str(num))
    num = num + 1

    mp = MPL3115A2(py,mode=ALTITUDE) # Returns height in meters. Mode may also be set to PRESSURE, returning a value in Pascals
    print("1- MPL3115A2 temperature: " + str(mp.temperature()))
    print("2- Altitude: " + str(mp.altitude()))
    mpp = MPL3115A2(py,mode=PRESSURE) # Returns pressure in Pa. Mode may also be set to ALTITUDE, returning a value in meters
    print("3- Pressure: " + str(mpp.pressure()))

    si = SI7006A20(py)
    print("4- Temperature: " + str(si.temperature())+ " deg C and Relative Humidity: " + str(si.humidity()) + " %RH")
    print("5- Dew point: "+ str(si.dew_point()) + " deg C")
    t_ambient = 24.4
    print("6- Humidity Ambient for " + str(t_ambient) + " deg C is " + str(si.humid_ambient(t_ambient)) + "%RH")

    lt = LTR329ALS01(py)
    print("7- Light (channel Blue lux, channel Red lux): " + str(lt.light()))

    li = LIS2HH12(py)
    print("8- Acceleration: " + str(li.acceleration()))
    print("Roll: " + str(li.roll()))
    print("Pitch: " + str(li.pitch()))

    print("9- Battery voltage: " + str(py.read_battery_voltage()))

    time.sleep(1)
    pycom.rgbled(0x7f0000) # red color for embedded led

    # every 5 seconds..
    time.sleep(5)
