# https://www.halvorsen.blog/documents/technology/iot/pico/pico_temperature_sensor_builtin.php
import machine
import time

from machine import Pin, I2C

# LCD
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

# End LCD

# The Raspberry Pi Pico seems to have a built in temperature sensor,
# which is very neat, I could monitor how hot it is near it.

# Temperature
adcpin = 4
sensor = machine.ADC(adcpin)

"""
    Get the temperature in a loop every second.
    This is set to output in Fahrenheit.
    I need to add an option to switch to Celsius in the code.
"""
def temperature_loop():
    while True:
        adc_value = sensor.read_u16()
        #volt = (3.3/65535) * adc_value
        volt = adc_value * (3.3/65535)

        tempC = 27 - (volt - 0.706) / 0.001721
        tempF = tempC * 1.8 + 32

        #print(f"Temperature in Celsius: {tempC}")
        #print(f"Temperature in Fahrenheit {tempF}")
        return tempF
        time.sleep(1)
    time.sleep(1)

"""
    Write the temperature sensor data to the connected 16x2 LCD screen.
    I have adapted this code from my other code and it works now.
"""
def write_to_lcd():
    while True:
        write_lcd(f"Temp: {temperature_loop()}", 0)
        time.sleep(1)

if __name__ == '__main__':    
    try:
        write_to_lcd()
    except KeyboardInterrupt:
        print("Clearing LCD")
        lcd.clear()
        pass

