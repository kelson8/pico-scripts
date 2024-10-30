# https://www.freva.com/find-out-an-i2c-address-with-the-raspberry-pi-pico/
import machine

sda = machine.Pin(0)
scl = machine.Pin(1)

i2c = machine.I2C(0, sda=sda, scl=scl, freq=400000)

print("I2C Address: ")
print(i2c.scan(), ' (decimal)')
print(hex(i2c.scan()[0]), ' (hex)')

