#!/usr/bin/env python
#
# Copyright (c) 2022, IUT / Université Jean-Monnet
#

import network
import time
from machine import RTC
import config

wlan = network.WLAN(mode=network.WLAN.STA)
wlan.connect(config.WIFI_SSID, auth=(network.WLAN.WPA2,config.WIFI_PASS))
while not wlan.isconnected():
    time.sleep_ms(50)
print("Wlan config= ",wlan.ifconfig())
rtc = RTC()
rtc.ntp_sync("pool.ntp.org",360)
while not rtc.synced():
    time.sleep_ms(50)
print("RTC= ",rtc.now())
