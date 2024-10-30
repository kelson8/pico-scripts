# https://electrocredible.com/raspberry-pi-pico-lcd-16x2-i2c-pcf8574-micropython/
import time
from machine import Pin, I2C

from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd

i2c_address = 0x27
i2c_num_rows = 2
i2c_num_cols = 16

sda = machine.Pin(0)
scl = machine.Pin(1)

i2c = I2C(0, sda=sda, scl=scl, freq=400000)
lcd = I2cLcd(i2c, i2c_address, i2c_num_rows, i2c_num_cols)
# Why was this needed? Seems to just slow it down.
#time.sleep(1)

# The text to write to, and the position
# If the LCD is a 2x16, this can either be 0 or 1.
def write_lcd(text, pos):
    lcd.clear()
    lcd.move_to(0, pos)
    lcd.putstr(text)

def print_welcome_msg():
    lcd.clear()
    lcd.move_to(0,0)
    lcd.putstr("Welcome to")

    lcd.move_to(0,1)
    lcd.putstr("KCNet systems")
    
print_welcome_msg()
time.sleep(2)
lcd.clear()




