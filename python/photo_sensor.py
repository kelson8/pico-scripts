# https://peppe8o.com/how-to-use-a-photoresistor-with-raspberry-pi-pico/
# https://www.coderdojotc.org/micropython/sensors/02-photosensor/
from machine import ADC, Pin
from time import sleep

photo_pin = machine.ADC(26)

while True:
    val = photo_pin.read_u16()
    print(val)
    sleep(.2)
