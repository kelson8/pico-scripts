from machine import Pin
import utime

# https://docs.sunfounder.com/projects/euler-kit/en/latest/pyproject/py_led_bar.html

pin = [17,18,19,20,21,22,26,27,28,15]
led = []
for i in range(10):
    led.append(None)
    led[i] = Pin(pin[i], machine.Pin.OUT)
    
led1 = Pin(17)
led2 = Pin(18)
led3 = Pin(19)
led4 = Pin(20)
led5 = Pin(21)
led6 = Pin(22)
led7 = Pin(26)
led8 = Pin(27)
led9 = Pin(28)
led10 = Pin(15)

#led1.toggle()
#led2.toggle()

def bar_graph_loop():
    while True:
        for i in range(10):
            led[i].toggle()
            utime.sleep(0.2)
            
def bar_graph_test1():
    led1.toggle()
    led4.toggle()
    
def bar_graph_test2():
    led2.toggle()
    led8.toggle()
    led10.toggle()
    
def bar_graph_test3():
    while True:
        led1.toggle()
        led3.toggle()
        led5.toggle()
        led7.toggle()
        led9.toggle()
        utime.sleep(0.8)
    
def turn_off_leds():
    for i in range(10):
        led[i].off()

def turn_on_leds():
    for i in range(10):
        led[i].on()

if __name__ == '__main__':
    try:
        #bar_graph_loop()
        #bar_graph_test1()
        #bar_graph_test2()
        #bar_graph_test3()
        
        turn_on_leds()
        utime.sleep(0.8)
        turn_off_leds()
    except KeyboardInterrupt:
        print("Exiting")

