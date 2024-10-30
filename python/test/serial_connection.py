import machine
import time

# https://timhanewich.medium.com/using-uart-between-a-raspberry-pi-pico-and-raspberry-pi-3b-raspbian-71095d1b259f

uart1 = machine.UART(1, baudrate=9600, tx=machine.Pin(4), rx=machine.Pin(5), timeout=1000)

while True:
    print(uart1.read(5))
    time.sleep(0.5)
