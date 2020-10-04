#!/usr/bin/env python
#
# example to connect to wifi network in base station mode STA
# please configure configWifi file before run

from network import WLAN
from mqtt import MQTTClient
import pycom
import machine
import time
import ubinascii
import config

pycom.heartbeat(True)

wlan = WLAN(mode=WLAN.STA)

# classical mac writing convention
print ("mac address = "+ ubinascii.hexlify(wlan.mac().sta_mac,':').decode())
strID = ubinascii.hexlify(wlan.mac().sta_mac,'').decode()
# hostname from the 4 last characters
hostNameID = "node_"+strID[-5:]
print("hostname = " + hostNameID)

nets = wlan.scan()

# connect process for network configuration in config file
if wlan.isconnected():
     print("config status: "+wlan.ifconfig())
else:
     for net in nets:
          if (net.ssid == config.WIFI_SSID):
               wlan.connect(net.ssid, auth=(net.sec, config.WIFI_PASS), timeout=5000, hostname=hostNameID)
               while not wlan.isconnected():
                    machine.idle() # save power while waiting
               print(wlan.ifconfig())
               print("Connected with IP address:" + wlan.ifconfig()[0])
               print(" & hostname: "+wlan.hostname())

# to suppress timeout error
def settimeout(duration): 
    pass

client = MQTTClient(hostNameID, config.MQTT_SERVER, port=1883)
client.settimeout = settimeout

#client.set_callback(sub_cb)
client.connect()

