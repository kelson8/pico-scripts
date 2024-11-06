from machine import Pin
from picozero import DigitalOutputDevice
import time

LSBFIRST = 1
MSBFIRST = 2

data_pin = DigitalOutputDevice(19)
latch_pin = DigitalOutputDevice(18)
clock_pin = DigitalOutputDevice(17)

#data_pin = DigitalOutputDevice(17)
#latch_pin = DigitalOutputDevice(18)
#clock_pin = DigitalOutputDevice(19)

# shiftOut function, use bit serial transmission.
def shiftOut(order,val):
    for i in range(0,8):
        clock_pin.off()
    if(order == LSBFIRST):
        data_pin.on() if (0x01&(val>>i)==0x01) else data_pin.off()
    elif(order == MSBFIRST):
        data_pin.on() if (0x80&(val<<i)==0x80) else data_pin.off()
        clock_pin.on()

def loop():
    while True:
        x=0x01
        for i in range(0, 8):
            latch_pin.off() # Output low level to latch pin
            shiftOut(LSBFIRST, x) # Send serial data to 74HC595
            latch_pin.on() # Output high level to latchPin and 74HC595 will update the data to the parallel output port.
            x <<=1 # make the variable move one bit to left once, then the bright LED move one step to the left once.
            time.sleep(0.5)
        x=0x80
        
        for i in range(0, 8):
            latch_pin.off()
            shiftOut(LSBFIRST, x)
            latch_pin.on()
            x >>= 1
            time.sleep(0.5)

def destroy():
    data_pin.close()
    latch_pin.close()
    clock_pin.close()
    
if __name__ == '__main__':
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
        print("Exiting")
            
            