import random
import time
from machine import Pin, I2C

from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd

# https://fuzzthepiguy.tech/password-generator/

# Basic password generator using a button that outputs to the python console and to a LCD screen.

button = Pin(20, Pin.IN, Pin.PULL_UP)

# LCD
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
    #lcd.clear()
    lcd.move_to(0, pos)
    lcd.putstr(text)
    
# Password Gen
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()"

def password_gen(length):
    #length = 16
    password = ''
    for c in range(length):
      password += random.choice(characters)
    # Print the password into console and return it for use on the LCD
    print(password)
    return password

write_lcd("Password: ", 0)
while True:
    if button.value() == 0:
        write_lcd(password_gen(16), 1)
        time.sleep(0.5)
    
#write_lcd(password_gen(16), 0)

#--------------------




