# pycom-ws2812
A module for Pycom hardware to use WS2812 RGB LEDs (commonly known as NeoPixels)
thanks to this repository : https://github.com/graham-mitchell-vcs/pycom-ws2812
hardware configuration and more informations on the tutorial at https://core-electronics.com.au/tutorials/WS2812_and_NeoPixel_with_Pycom.html 

@IUTSE : LED project.. in main.py
- infinite loop with 3 steps only white, blue, red on neopixel and wipy internal LED with 5s between each color 
- hardware : wipy on expansion board, neopixel 8 LEDs, and connected at 3.3V & P11 for driving signal

This module is designed for use on the Pycom Wipy and Lopy4 and gives functionality to drive WS2812s (NeoPixels)
Animation functions have been added to the main.py file to make it easy to create fun patterns.
Some of these patterns were translated from the NeoPixel StrandTest, and some were made up!

The files used are:
library to drive the NeoPixel LED
    ws2812.py
to test the code :
    boot.py and main.py are blank.. only test
    test.py is the original file with some amazing led animation.. 
    animations.py is the library of the visual animationd you can find in test.py
    colorBlue, colorRed, and colorWhite : experiment simplest way 

# Set the number of LEDs
numLed = 8

Change this to the number of LEDs in your strip.

# Initialize LEDs
chain = WS2812( ledNumber=numLed, brightness=10, dataPin='P11' ) # dataPin is for LoPy board only

The brightness value will needs to be 1-100, and can be changed later on.
The default pin is P11. On the Lopy4 this can be assigned to other pins
P11 is G22 on the Expansion Board 3.0
 
Call the Animation functions in the main loop of test.py !!
call the only color..

use the CTRL^C to finish the main loop... but be carefull : only stop the program and the LAED stand by the latest color !
