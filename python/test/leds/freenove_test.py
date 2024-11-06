#!/usr/bin/env python3
#############################################################################
# Filename    : SevenSegmentDisplay.py
# Description : Control SevenSegmentDisplay with 74HC595
# Author      : www.freenove.com
# modification: 2023/05/15
########################################################################
from machine import Pin
from picozero import DigitalOutputDevice

import utime
import random
import time

LSBFIRST = 1
MSBFIRST = 2
# define the pins for 74HC595





dataPin   = 17
latchPin  = 18
clockPin  = 19

# dataPin=Pin(dataPin, Pin.OUT)
# latchPin=Pin(latchPin, Pin.OUT)
# clockPin=Pin(clockPin, Pin.OUT)

dataPin=DigitalOutputDevice(dataPin, Pin.OUT)
latchPin=DigitalOutputDevice(latchPin, Pin.OUT)
clockPin=DigitalOutputDevice(clockPin, Pin.OUT)

# SevenSegmentDisplay display the character "0"- "F" successively
num = [0xc0,0xf9,0xa4,0xb0,0x99,0x92,0x82,0xf8,0x80,0x90,0x88,0x83,0xc6,0xa1,0x86,0x8e]

def shiftOut(order,val):
    for i in range(0,8):
        clockPin.off()
        if(order == LSBFIRST):
            dataPin.on() if (0x01&(val>>i)==0x01) else dataPin.off()
        elif(order == MSBFIRST):
            dataPin.on() if (0x80&(val<<i)==0x80) else dataPin.off()
        clockPin.on()

def loop():
    while True:
        for i in range(0,len(num)):
            latchPin.off()
            shiftOut(MSBFIRST,num[i])  # Send serial data to 74HC595
            latchPin.on()
            time.sleep(0.5)
        for i in range(0,len(num)):
            latchPin.off()
            shiftOut(MSBFIRST,num[i]&0x7f) # Use "&0x7f" to display the decimal point.
            latchPin.on()
            time.sleep(0.5)

def destroy():  
    dataPin.close()
    latchPin.close()
    clockPin.close() 

if __name__ == '__main__': # Program entrance
    print ('Program is starting...' )
    try:
        loop()  
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()
        print("Ending program")
