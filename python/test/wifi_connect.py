import time
import network
import secrets

# This is untested

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
#wlan.connect(secrets.ssid, secrets.password)

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
        print(status)
        print(f"Ip: {status[0]}")

def disconnect_network():
    wlan.disconnect()

    