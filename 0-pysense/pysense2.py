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

    lt = LTR329ALS01(py) # I2C sensor acquisition
    print("7- Light (channel Blue lux, channel Red lux): " + str(lt.light()))

    time.sleep(1)
    pycom.rgbled(0x7f0000) # red color for embedded led

    time.sleep(5)

