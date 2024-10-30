# https://www.halvorsen.blog/documents/technology/iot/pico/pico_temperature_sensor_builtin.php
import machine
import time

# The Raspberry Pi Pico seems to have a built in temperature sensor,
# which is very neat, I could monitor how hot it is near it.

adcpin = 4
sensor = machine.ADC(adcpin)

adc_value = sensor.read_u16()
volt = (3.3/65535) * adc_value

tempC = 27 - (volt - 0.706) / 0.001721
tempF = tempC * 1.8 + 32
print(f"Temperature in Celsius: {tempC}")
print(f"Temperature in Fahrenheit {tempF}")
