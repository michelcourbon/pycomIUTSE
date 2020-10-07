#!/usr/bin/env python
#
# example to connect to wifi network in base station mode STA
# please configure configWifi file before run

from network import WLAN
import pycom
import machine
import ubinascii
import configWifi

pycom.heartbeat(True)

wlan = WLAN(mode=WLAN.STA)

# classical mac writing convention
print ("mac address = "+ ubinascii.hexlify(wlan.mac().sta_mac,':').decode())
strID = ubinascii.hexlify(wlan.mac().sta_mac,'').decode()
# hostname from the 4 last characters
hostNameID = "N"+strID[-5:]
print("hostname = " + hostNameID)


nets = wlan.scan()
# list all enable ssid
for net in nets:
     print('Network found with ssid : '+net.ssid)     
print('scanning SSID finished !!')

# connect process for network configuration in configWifi file
if wlan.isconnected():
     print(wlan.ifconfig())
else:
     for net in nets:
          if (net.ssid == configWifi.WIFI_SSID):
               wlan.connect(net.ssid, auth=(net.sec, configWifi.WIFI_PASS), timeout=5000, hostname=hostNameID)
               while not wlan.isconnected():
                    machine.idle() # save power while waiting
               print(wlan.ifconfig())
               print("Connected with IP address:" + wlan.ifconfig()[0])
               print(" & hostname: "+wlan.hostname())
