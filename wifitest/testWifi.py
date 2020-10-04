#!/usr/bin/env python
#
# example to connect to wifi network in base station mode STA
# please configure configWifi file before run

from network import WLAN
import machine
import configWifi

pycom.heartbeat(True)

wlan = WLAN(mode=WLAN.STA)
print ("your device mac address")
print(ubinascii.hexlify(wlan.mac().sta_mac,':').decode())
macAddress = machine.unique_id()
print("MAC address is " + macAddress)

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
               wlan.connect(net.ssid, auth=(net.sec, configWifi.WIFI_PASS), timeout=5000)
               while not wlan.isconnected():
                    machine.idle() # save power while waiting
               print(wlan.ifconfig())
               print("Connected with IP address:" + wlan.ifconfig()[0])
