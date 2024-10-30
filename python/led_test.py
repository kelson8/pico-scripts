from picozero import LED
from time import sleep

# Taken some code from 16x2_lcd.py
# https://electrocredible.com/raspberry-pi-pico-lcd-16x2-i2c-pcf8574-micropython/
import time
from machine import Pin, I2C

from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd

# I2C and LCD
i2c_address = 0x27
i2c_num_rows = 2
i2c_num_cols = 16

sda = machine.Pin(0)
scl = machine.Pin(1)

i2c = I2C(0, sda=sda, scl=scl, freq=400000)
lcd = I2cLcd(i2c, i2c_address, i2c_num_rows, i2c_num_cols)
# Why was this needed? Seems to just slow it down.
#time.sleep(1)

# LED
yellow = LED(18)

def write_to_lcd():
    lcd.clear()
    lcd.move_to(0,0)
    lcd.putstr("Led Status: ")
    
    #lcd.move_to(0,1)
    lcd.putstr("Off")
    sleep(0.5)
    
    lcd.clear()
    lcd.move_to(0,0)
    lcd.putstr("Led Status: ")
    lcd.putstr("On")

    #lcd.move_to(0,1)
    #lcd.putstr("KCNet systems")



def toggle_led():
    yellow.on()
    sleep(0.5)
    yellow.off()
    sleep(0.5)

while True:
    toggle_led()
    write_to_lcd()
    
