import time
import network
import secrets

# Ping
import uping

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
#wlan.connect(secrets.ssid, secrets.password)

# Toggle this to display the IP Address, Subnet mask, Gateway, and DNS.
verbose_status = False

# Connect to the wifi using the ssid and password stored in the secrets file
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
        if verbose_status:
            print(f"IP Address: {status[0]}")
            print(f"Subnet Mask: {status[1]}")
            print(f"Gateway: {status[2]}")
            print(f"DNS: {status[3]}")

# Disconnect from the wifi
def disconnect_network():
    wlan.disconnect()
    
def ping_server(server):
    try:
        connect_network()
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
