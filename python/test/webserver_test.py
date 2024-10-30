import time
import network
import secrets
import socket

from picozero import LED
from machine import Pin

# LED
yellow_led = LED(18)

# https://www.raspberrypi.com/news/how-to-run-a-webserver-on-raspberry-pi-pico-w/
# Slightly modified from wifi_connect.py

# Good guide on using html files:
# https://www.tomshardware.com/how-to/raspberry-pi-pico-w-web-server

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
#wlan.connect(secrets.ssid, secrets.password)

#html = """<!DOCTYPE html>
#<html>
#    <head> <title>Pico W</title> </head>
#    <body> <h1>Pico W</h1>
#        <button> Yellow Led On </button>
#        <button> Yellow Led Off </button>
#        <p>%s</p>
        
#    </body>
#</html>
#"""

# TODO Fix this to work with a html file and
# activating a led using a button in html

# New
#page = open("index.html", "r")
#html = page.read()
#page.close()
#

def connect_network():
    wlan.connect(secrets.ssid, secrets.password)
    
    # Wait for connection or failure
    max_wait = 10
    while max_wait > 0:
        if wlan.status() < 0 or wlan.status() >= 3:
            break
        max_wait -= 1
        print("Waiting for connection")
        time.sleep(1)
        
    # Handle connection error
    if wlan.status() != 3:
        raise RuntimeError("Network connection failed")
    else:
        print(f"Connected to network {secrets.ssid}")
        status = wlan.ifconfig()
        #print(status)
        print(f"IP Address: {status[0]}")
        print(f"Subnet Mask: {status[1]}")
        print(f"Gateway: {status[2]}")
        print(f"DNS: {status[3]}")


# First connect to the network.
connect_network()

# Then set the address and socket
status = wlan.ifconfig()
addr = socket.getaddrinfo("0.0.0.0", 80)[0][-1]
s = socket.socket()
# https://github.com/micropython/micropython/issues/3739#issuecomment-386191815
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind(addr)
s.listen(1)
print (f"Listening on {status[0]}")

# Function to load in html page
# https://github.com/pi3g/pico-w/blob/main/MicroPython/I%20Pico%20W%20LED%20web%20server/main.py
def get_html(html_name):
    with open(html_name, 'r') as file:
        html = file.read()
        
    return html

# I finally got this working!
# 10-30-2024 @ 12:11AM

# This turns on/off the yellow led on pin 18 on the RPI Pico.
def webpage_loop():
    while True:
        try:
            cl, addr = s.accept()
            
            # Old
            #cl_file = cl.makefile('rwb', 0)
            #while True:
            #    line = cl_file.readline()
            #    if not line or line == b'\r\n':
            #        break
            #
            
            print("Client connected from", addr)
            r = cl.recv(1024)
            #print(r)
            
            r = str(r)
            led_on = r.find("?led=on")
            led_off = r.find("?led=off")
            
            #stateis = ""
            #if led_on == 6:
            if led_on > -1:
                print("Led is on")
                yellow_led.on()
                #stateis = "LED is ON"
                
            #if led_off == 6:
            if led_off > -1:
                print("Led is off")
                yellow_led.off()
                #stateis = "LED is OFF"
            
            #response = html % stateis
            
            #response = html
            response = get_html("index.html")
            
            cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
            cl.send(response)
            cl.close()
            
        except OSError as e:
            #cl.close()
            print("Connection closed")
            
# Run the webpage loop
webpage_loop()

# Kill the socket when done
#s.close()

def disconnect_network():
    wlan.disconnect()
    

