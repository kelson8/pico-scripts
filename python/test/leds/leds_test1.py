from machine import Pin
#from picozero import DigitalOutputDevice
import utime
import random

# https://peppe8o.com/how-to-use-74hc595-shift-register-with-raspberry-pi-pico-and-micropython/

# This works now! I think I had the 74hc595 wired in reverse before.

# TODO Figure out how to use this to turn off the LED's, I tried a couple of things with it.

dataPIN = 17
latchPIN = 18
clockPIN = 19

dataPIN=Pin(dataPIN, Pin.OUT)
latchPIN=Pin(latchPIN, Pin.OUT)
clockPIN=Pin(clockPIN, Pin.OUT)

# dataPIN=DigitalOutputDevice(dataPIN, Pin.OUT)
# latchPIN=DigitalOutputDevice(latchPIN, Pin.OUT)
# clockPIN=DigitalOutputDevice(clockPIN, Pin.OUT)

def shift_update(shift_input, data, clock, latch):
    # Put latch down to start data sending
    clock.value(0)
    latch.value(0)
    clock.value(1)
      
      # Load data in reverse order
    for i in range(7, -1, -1):
        clock.value(0)
        data.value(int(shift_input[i]))
        clock.value(1)

    # Put latch up to store data on register
    clock.value(0)
    latch.value(1)
    clock.value(1)
  
def turn_off_leds(shift_input, data, clock, latch):
    # Put latch down to start data sending
    clock.value(0)
    latch.value(0)
    clock.value(1)
          
    for i in range(7, -1, -1):
        clock.value(0)
        #data.value(int(shift_input[i]))
        #clock.value(1)
            
        
    clock.value(0)
    latch.value(1)
    clock.value(1)
    
  


def main_loop():
    bit_string="00000000"
    while True:
        shift_update(bit_string, dataPIN, clockPIN, latchPIN)
        bit_string = str(random.randint(0, 1)) + bit_string[:-1]
        utime.sleep(0.3)
        print_values()
       
def destroy(data, clock, latch):
    #clockPIN.off()
    #latchPIN.off()
    #dataPIN.off()
    
    clock.value(0)
    latch.value(0)
    data.value(0)
    clock.value(1)

def print_values():
    clock_value = clockPIN.value()
    latch_value = latchPIN.value()
    data_value = dataPIN.value()
    print(f"Clock: {clock_value}\n Latch: {latch_value}\n Data: {data_value}")

if __name__ == '__main__':
    bit_string="00000000"
    try:
        main_loop()
        #destroy(dataPIN, clockPIN, latchPIN)
        #turn_off_leds(bit_string, dataPIN, clockPIN, latchPIN)
        #print_values()
        
    except KeyboardInterrupt:
        print("Exiting!")



