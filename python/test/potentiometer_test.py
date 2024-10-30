from picozero import Pot
from time import sleep

# LCD
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

# The text to write to, and the position
# If the LCD is a 2x16, this can either be 0 or 1.
def write_lcd(text, pos):
    #lcd.clear()
    lcd.move_to(0, pos)
    lcd.putstr(text)
#

# https://projects.raspberrypi.org/en/projects/introduction-to-the-pico/11
dial = Pot(1) # Connected to pin A1 (GP_27)

def cleanup():
    print("Exiting and clearing LCD.")
    lcd.clear()

print_volts = False

def main():
    while True:
        volts = dial.voltage
        print(f"Value: {dial.value}\n")
        print(f"Voltage: {dial.voltage}")
    
    
        # Basic test to print off the values if the voltage is at a certain point
        if print_volts:
            if volts >= 1.6 and volts <=1.7:
                print("1.6v reached")
    
            if volts == 3.3:
                print("Highest point reached")
    
        # This doesn't seem to exist for some reason
        #print(f"Percent: {dial.percent}")
        str_dial_value = str(dial.value)
        write_lcd(str_dial_value, 0)
        sleep(0.5)
        lcd.clear()       

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        # Clear the LCD screen on exit
        cleanup()
    


