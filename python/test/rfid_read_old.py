from mfrc522 import MFRC522
import utime

# New
from picozero import LED

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

# The text to write to, and the position
# If the LCD is a 2x16, this can either be 0 or 1.
def write_lcd(text, pos):
    lcd.clear()
    lcd.move_to(0, pos)
    lcd.putstr(text)

# LED
yellow = LED(18)

#
 
# https://how2electronics.com/using-rc522-rfid-reader-module-with-raspberry-pi-pico/
reader = MFRC522(spi_id=0,sck=6,miso=4,mosi=7,cs=5,rst=22)
 
# This works.
# TODO Try to change the pins to be closer together if possible.

print("Bring TAG closer...")
print("")
 
 
while True:
    reader.init()
    (stat, tag_type) = reader.request(reader.REQIDL)
    if stat == reader.OK:
        (stat, uid) = reader.SelectTagSN()
        if stat == reader.OK:
            card = int.from_bytes(bytes(uid),"little",False)
            if card == 3545142044:
                #print("RFID Key Fob")
                print("Authorized to area #1")
                yellow.on()
                write_lcd("Access granted.", 0)
                utime.sleep_ms(1000)
                yellow.off()
                lcd.clear()
            elif card == 189660443:
                #print("RFID Card")
                print("Authorized to area #2")
            #else:
            #    print("Not authorized")
            #print("CARD ID: "+str(card))
            utime.sleep_ms(500)
 
