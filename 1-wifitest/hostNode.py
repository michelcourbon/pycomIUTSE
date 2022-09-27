#!/usr/bin/env python
#
# example to connect to wifi network in base station mode STA

from network import WLAN
import ubinascii 

wlan = WLAN(mode=WLAN.STA)
# classical mac writing convention
print ("mac address = "+ ubinascii.hexlify(wlan.mac().sta_mac,':').decode())
strID = ubinascii.hexlify(wlan.mac().sta_mac,'').decode()
# hostname from the 4 last characters
hostName = "node_"+strID[-5:]
print("hostname = " + hostName)
