from machine import Pin, ADC, I2C
import utime

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

# https://www.tomshardware.com/how-to/raspberry-pi-pico-joystick
xAxis = ADC(Pin(27))
yAxis = ADC(Pin(26))

button = Pin(22, Pin.IN, Pin.PULL_UP)

write_to_lcd = False
while True:
    xValue = xAxis.read_u16()
    yValue = yAxis.read_u16()
    buttonValue = button.value()
    # Not sure how to get this to properly clear the LCD.
    # lcd.clear makes it laggy.
    if write_to_lcd:
        write_lcd(f"X: {str(xValue)}", 0)
        write_lcd(f"Y: {str(yValue)}", 1)
        utime.sleep(0.5)
        #lcd.clear()
    
    button_is_pressed = "No"
    if buttonValue == 0:
        button_is_pressed = "Yes"
    elif buttonValue == 1:
        button_is_pressed = "No"
        
    
    #print(f"X: {str(xValue)}\n Y: {str(yValue)}\n Button: {str(buttonValue)}")
    print(f"X: {str(xValue)}\n Y: {str(yValue)}\n Button Pressed: {button_is_pressed}")
    utime.sleep(0.5)