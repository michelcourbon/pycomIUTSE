from ws2812 import WS2812
import utime
import uos
import pycom

# disable LED heartbeat (probably not needed in this application)
pycom.heartbeat(False)

# set the number of LEDs onto the strip
numLed = 8

# initialize LEDs
chain = WS2812( ledNumber=numLed, brightness=10, dataPin='P11' ) # dataPin is for LoPy board only
# initialize LEDs to White
wait = 5000

while True:
    # white
    pycom.rgbled(0x7f7f7f)
    data = [(255,255,255)] * numLed
    chain.show( data )
    utime.sleep_ms(wait)
    # blue
    pycom.rgbled(0x00007f)
    data = [(255,0,0)] * numLed
    chain.show( data )
    utime.sleep_ms(wait)
    # red
    pycom.rgbled(0x7f0000)
    data = [(0,0,255)] * numLed
    chain.show( data )
    utime.sleep_ms(wait)

