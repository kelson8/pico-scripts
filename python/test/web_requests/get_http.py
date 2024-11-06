import network
import wifi_secrets
import rp2

import urequests

from picozero import LED
import time

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
#wlan.connect(secrets.ssid, secrets.password)

# Add the country for wifi, set to US
rp2.country("US")

power_led = LED(19)

# Disable power saving mode with a toggle.
disable_power_save = False
if disable_power_save:
    wlan.config(pm = 0xa11140)
    
"""
    Turns on the power led on pin 19
"""
def toggle_power_led():
    power_led.on()

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
        #status = wlan.ifconfig()
        #print(status)
        #print(f"Ip: {status[0]}")
    
# This is untested.
# Make a get request to a website
"""
    Url to use
    Https enabled, true/false
    If https is enabled this adds "https://" to the url, otherwise it adds "http://"
"""
def get_request(url, https):
    if https:
        #print(f"https://{url}")
        r = urequests.get(f"https://{url}")
        print(r.content)
        r.close()
    else:
        r = urequests.get(f"http://{url}")
        print(r.content)
        r.close()
    
# Set as invalid site, can be changed
local_website = "localsite.net"


if __name__ == '__main__':
    connect_network()
    
    toggle_power_led()
    get_request(local_website, True)

