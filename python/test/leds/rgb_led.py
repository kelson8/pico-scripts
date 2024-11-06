import machine
import utime

# https://docs.sunfounder.com/projects/euler-kit/en/latest/pyproject/py_rgb.html

red = machine.PWM(machine.Pin(17))
green = machine.PWM(machine.Pin(18))
blue = machine.PWM(machine.Pin(19))
red.freq(1000)
green.freq(1000)
blue.freq(1000)

def interval_mapping(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def color_to_duty(rgb_value):
    rgb_value = int(interval_mapping(rgb_value,0,255,0,65535))
    return rgb_value

def color_set(red_value,green_value,blue_value):
    red.duty_u16(color_to_duty(red_value))
    green.duty_u16(color_to_duty(green_value))
    blue.duty_u16(color_to_duty(blue_value))

color_set(222,2,2)
