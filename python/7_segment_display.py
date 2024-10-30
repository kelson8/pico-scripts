# https://www.youngwonks.com/blog/How-to-use-a-7-segment-LED-display-with-the-Raspberry-Pi-Pico
# https://electrocredible.com/7-segment-display-with-raspberry-pi-pico/
from machine import Pin
import utime

# This doesn't proplerly work, display number says out of range and
# the print value under display_number says out of range.

pins = [
    Pin(16, Pin.OUT), # Middle
    Pin(17, Pin.OUT), # Top left
    Pin(18, Pin.OUT), # Top
    Pin(19, Pin.OUT), # Top right
    Pin(13, Pin.OUT), # Bottom right
    Pin(14, Pin.OUT), # Bottom
    Pin(15, Pin.OUT), # Bottom left
    Pin(12, Pin.OUT), # Dot
    ]

# Pin states for each digit to display numbers 0-9
number_map = [
    [1, 1, 1, 1, 1, 1, 0],  # 0
    [0, 1, 1, 0, 0, 0, 0],  # 1
    [1, 1, 0, 1, 1, 0, 1],  # 2
    [1, 1, 1, 1, 0, 0, 1],  # 3
    [0, 1, 1, 0, 0, 1, 1],  # 4
    [1, 0, 1, 1, 0, 1, 1],  # 5
    [1, 0, 1, 1, 1, 1, 1],  # 6
    [1, 1, 1, 0, 0, 0, 0],  # 7
    [1, 1, 1, 1, 1, 1, 1],  # 8
    [1, 1, 1, 1, 0, 1, 1]   # 9
]

def display_number(number):
    segments_values = number_map[number]
    for i in range(len(pins)):
        print(pins[i].value(segments_values[i]))
        #pins[i].value(segments_values[i])
 
display_number(2)
 
#while True:
#    for number in range(10):
#        display_number(number)
#        utime.sleep_ms(1000)
