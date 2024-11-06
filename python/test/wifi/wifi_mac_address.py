import network
import ubinascii

# This works

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
mac = ubinascii.hexlify(network.WLAN().config("mac"), ":").decode()
print(mac)

# Other things to query
#print(wlan.config("channel"))
#print(wlan.config("essid"))
#print(wlan.config("power"))

