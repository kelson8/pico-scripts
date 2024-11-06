import machine
import time

# https://docs.sunfounder.com/projects/euler-kit/en/latest/pyproject/py_74hc595_7seg.html

SEGCODE = [0x3f,0x06,0x5b,0x4f,0x66,0x6d,0x7d,0x07,0x7f,0x6f]

dataPIN = 17
latchPIN = 18
clockPIN = 19

#dataPIN = 19
#latchPIN = 18
#clockPIN = 17

sdi = machine.Pin(dataPIN,machine.Pin.OUT)
rclk = machine.Pin(latchPIN,machine.Pin.OUT)
srclk = machine.Pin(clockPIN,machine.Pin.OUT)

def hc595_shift(dat):
    rclk.low()
    time.sleep_ms(5)
    for bit in range(7, -1, -1):
        srclk.low()
        time.sleep_ms(5)
        value = 1 & (dat >> bit)
        sdi.value(value)
        time.sleep_ms(5)
        srclk.high()
        time.sleep_ms(5)
    time.sleep_ms(5)
    rclk.high()
    time.sleep_ms(5)

while True:
    for num in range(10):
        hc595_shift(SEGCODE[num])
        time.sleep_ms(500)
