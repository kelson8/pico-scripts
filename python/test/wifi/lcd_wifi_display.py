import time
from machine import Pin, I2C

from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd

# Networking/Wifi
import network
#import secrets

from wifi_connect import connect_network, disconnect_network

import uping

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
#

# LCD
i2c_address = 0x27
i2c_num_rows = 2
i2c_num_cols = 16

sda = machine.Pin(0)
scl = machine.Pin(1)

i2c = I2C(0, sda=sda, scl=scl, freq=400000)
lcd = I2cLcd(i2c, i2c_address, i2c_num_rows, i2c_num_cols)
#
    
# The text to write to, and the position
# If the LCD is a 2x16, this can either be 0 or 1.
def write_lcd(text, pos):
    #lcd.clear()
    lcd.move_to(0, pos)
    lcd.putstr(text)
    
def display_ip_info():
    #lcd.clear()
    # Try to connect to the network, fail if no connection
    #try:
        connect_network(False)
        status = wlan.ifconfig()
        # Oops my SSID is too long lol
        # TODO Setup scrolling text for ssid and ip
        #write_lcd(f"SSID: {secrets.ssid}", 0)
        write_lcd(f"Wifi connected", 0)
        # I had to remove the spacing for it to not overlap, I need a LCD that is a bit bigger.
        write_lcd(f"IP:{status[0]}", 1)
        print(f"IP:{status[0]}")
        
        # TODO Change this to ping a local website or something to display if it is online.
        webserver_status = False
        # Sleep fora couple seconds
        time.sleep(2)
        lcd.clear()
        write_lcd("Web server: ", 0)
        if webserver_status:
            write_lcd(f"Online", 1)
        else:
            write_lcd(f"Offline", 1)
        
    #except Exception as e:
    #    print(e)
    #    pass
    
    # Do a little error checking, this won't do anything if not connected.
    # TODO Is this needed? I'm doing this in the connection.
    #if wlan.status != 3:
    #    raise RuntimeError("Network connection failed!")
    #else:


def ping_server(server):
    try:
        connect_network(False)
        
        # TODO Figure out how to make this say connected if online, disconnected if offline.
        # Also I would like to display the website status on the rpi pico LCD
        #if webserver_connected:
        test_ping = uping.ping(server, count=4, timeout=5000, interval=10, quiet=False, size=64)
        # Ohh this is where the transmitted and received packets come from, I could use this
        #print(test_ping)
        
        if test_ping[1] == 0:
            print("Ping failure")
        else:
            print("Ping success!")
        
        #write_lcd(f"{test_ping}", 0)
        # Hmm, I wonder how to make this work.
        #if test_ping:
        #    print("Success")
        #else:
        #    print("Failure")
    except Exception as e:
        print(e)

# IP of pi-hole, this should mostly always be online.
#ip_addr = "192.168.1.36"
ip_addr = "10.2.2.2"
ping_server(ip_addr)



