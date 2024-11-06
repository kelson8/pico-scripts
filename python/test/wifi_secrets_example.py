# Rename this file to wifi_secrets.py for it to work properly.

# Change these values to match your network setup.
ssid = "Wifi SSID"
password = "Wifi Password"

# This seems to work, tested in PyCharm under a different script.
static_ip = True
# Whether to print all the values to the console.
print_details = False

if static_ip:
    ip = "192.168.1.x"
    netmask = "255.255.255.0"
    gateway = "192.168.1.x"


    # Set your preferred DNS here, only one should be enabled.
    # I have a Pi-Hole running so I point to it to use my internal domains and stuff.
    google_dns = False
    cloudflare_dns = True
    local_dns = False

    if google_dns:
        dns = "8.8.8.8"
    elif cloudflare_dns:
        dns = "1.1.1.1"
    elif local_dns:
        dns = "192.168.1.x"
        
    if print_details:
        # I always forget I can make multi line strings like this
        print(f"""IP: {ip}
Netmask: {netmask}
Gateway: {gateway}
DNS: {dns}
    """)
    