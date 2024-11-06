import time
import network
import wifi_secrets

# This seems to work

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
#wlan.connect(wifi_secrets.ssid, wifi_secrets.password)

# Connect to the wifi using the ssid and password stored in the wifi_secrets file
def connect_network():
    wlan.connect(wifi_secrets.ssid, wifi_secrets.password)
    
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
        print(f"Connected to network {wifi_secrets.ssid}")
        status = wlan.ifconfig()
        #print(status)
        print(f"IP Address: {status[0]}")
        print(f"Subnet Mask: {status[1]}")
        print(f"Gateway: {status[2]}")
        print(f"DNS: {status[3]}")

# Disconnect from the wifi
def disconnect_network():
    wlan.disconnect()
    

#if __name__ == '__main__':
#    connect_network()
    

