# pycomIUTSE
pycom examples folders : wipy mount on pysense board, to use in classroom experience 
- 0-pysense : pysense1 to test all sensors (embedded on pysense board) and pysense2 to test only one sensor more easy to visualize on scope the I2C frame (sensor is light sensor)
- 3-wifitest : test wifi connexion to access point (modify config file according your access point ip and security keys)
- 4-mqttsensor : test the connexion to a mqtt server via wifi
- 5-pycom-neopixel : example to drive neopixel LED (hardware : expansion board & neopixel LED)
- 6-mqttPysense : example to send json string containing sensors (from pysense hardware) to mqtt server

all examples tested with WIPY, usage of this repository :
- download zip file (or git clone)
- open the example folder you want try with Vscode (with pymakr extension) 
- modify config (wifi and mqtt), and upload one of this folders in the wipy memory
- open in the editor window, the python macro you wish to test
- run .. & that's all
