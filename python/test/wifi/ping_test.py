import time
import network
import wifi_secrets

from wifi_connect import connect_network, disconnect_network

# Ping
import uping

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
#wlan.connect(wifi_secrets.ssid, wifi_secrets.password)

# Disable power saving mode with a toggle.
disable_power_save = True
if disable_power_save:
    wlan.config(pm = 0xa11140)

# Toggle this to display the IP Address, Subnet mask, Gateway, and DNS.
verbose_status = False
    
# TODO Why does this drop packets?
def ping_server(server):
    try:
        connect_network(False)
        #uping.ping(server, count=1, timeout=5000, interval=10, quiet=False, size=64)
        
        # TODO Figure out how to make this say connected if online, disconnected if offline.
        # Also I would like to display the website status on the rpi pico LCD
        #if webserver_connected:
        test_ping = uping.ping(server, count=4, timeout=5000, interval=10, quiet=False, size=64)
        # Hmm, I wonder how to make this work.
        #if test_ping:
        #    print("Success")
        #else:
        #    print("Failure")
    except Exception as e:
        print(e)

# IP of pi-hole, this should mostly always be online.
ip_addr = "192.168.1.36"
#ip_addr = "10.2.2.2"
ping_server(ip_addr)
