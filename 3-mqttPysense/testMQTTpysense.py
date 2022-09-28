#!/usr/bin/env python
#
# Copyright (c) 2022, IUT / Université Jean-Monnet
#
import config
import ubinascii
import network
import time
import machine

# import mqtt tools
from umqtt.simple2 import MQTTClient

# import sensor library
from SI7006A20 import SI7006A20
from pysense import Pysense

#----- wlan ------------
def wlanConnect():
    wlan = network.WLAN(mode=network.WLAN.STA)    
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect(config.WIFI_SSID, auth=(network.WLAN.WPA2,config.WIFI_PASS))
        while not wlan.isconnected():
            time.sleep(1)
            pass
    print('Wlan network config : ', wlan.ifconfig())

#------ uid from wifi Mac address ------
def NodeUid ():
    wlan = network.WLAN(mode=network.WLAN.STA)
    idHard = ubinascii.hexlify(wlan.mac().sta_mac)
    return idHard

#--- float random number in range (mini,maxi) ----
def rand(mini, maxi):
    maxValue = 16777216
    val = machine.rng()
    resu = mini + (maxi-mini) * float(val) / maxValue
    return resu

#--------------- main -------------------

py = Pysense()
wlanConnect()

mqttId = NodeUid()
topic = NodeUid()+ b'/sensors'
print("topic : ",topic, type(topic))

client = MQTTClient(client_id=mqttId,server=config.MQTT_SERVER,port=1883,user=config.MQTT_USER,password=config.MQTT_PASS)
client.set_last_will(topic=topic, msg='lastWill', retain=False, qos=0)
client.connect()
time.sleep(1)
print ("connected to MQTT server")

while True:
    si = SI7006A20(py)
    temp = str(round(si.temperature(),2))
    hum = str(round(si.humidity(),1))

    JsonString = '{"Temperature":xx,"Humidite":yy}'
    JsonString = JsonString.replace("xx",temp)
    JsonString = JsonString.replace("yy",hum)

    MqttMsg = bytes(JsonString, 'utf-8')
    try:
        client.publish(topic, MqttMsg, retain=False, qos=0)
        print("publish : ",MqttMsg)
    except:
        print("Can not publish message - reconnecting")
        client.disconnect()
        time.sleep(1)
        client.connect()
    time.sleep(5)
