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

# this is compiling the file ready when requested
def get_request_file(request_file_name):
    file_requested = open(request_file_name, 'r').read()
    return file_requested

# this is getting the content length FOR IMAGES
def get_image_length(request_file_name):
    file_requested = open(request_file_name, 'rb').read()
    image_length = str(len(file_requested))
    return image_length


# This code works but it needs the "index.html" manually added to work.
# Not sure how to redirect it.
def webpage_loop():
    while True:
        try:
            cl, addr = s.accept()
            # New
            #cl_file = cl.makefile('rwb', 0)
            #while True:
            #    line = cl_file.readline()
            #    if not line or line == b'\r\n':
            #        break
            #
            
            print("Client connected from", addr)
            request = cl.recv(1024)
            
            # New
            # https://github.com/doncoop/pico-web-server/blob/main/webserver.py
            # Turn the request into a string
            request = str(request)
            
            if request == "/":
                request = request + "index.html"
            
            try:
                request = request.split()[1]
            except IndexError:
                pass
            
            # Works out what the file type of the request is so we send back the file as the correct MIME type
            if '.html' in request:
                file_header = 'HTTP/1.1 200 OK\r\nContent-type: text/html\r\n\r\n'
            elif '.css' in request:
                file_header = 'HTTP/1.1 200 OK\r\nContent-Type: text/css\r\n\r\n'
            elif '.js' in request:
                file_header = 'HTTP/1.1 200 OK\r\nContent-Type: text/javascript\r\n\r\n'
            elif '.svg' in request:
                image_length = get_image_length(request)
                file_header = 'HTTP/1.1 200 OK\r\nContent-Type: image/svg+xml\r\nContent-Length: ' + image_length + '\r\n\r\n'
            elif '.svgz' in request:
                file_header = 'HTTP/1.1 200 OK\r\nContent-Type: image/svg+xml\r\nContent-Length: ' + image_length + '\r\n\r\n'
            elif '.ico' in request:
                image_length = get_image_length(request)
                file_header = 'HTTP/1.1 200 OK\r\nContent-Type: image/x-icon\r\nContent-Length: ' + image_length + '\r\n\r\n'
            elif '.jpg' in request:
                image_length = get_image_length(request)
                file_header = 'HTTP/1.1 200 OK\r\nContent-Type: image/jpg\r\nContent-Length: ' + image_length + '\r\n\r\n'
            elif '.jpeg' in request:
                image_length = get_image_length(request)
                file_header = 'HTTP/1.1 200 OK\r\nContent-Type: image/jpeg\r\nContent-Length: ' + image_length + '\r\n\r\n'
            elif '.png' in request:
                image_length = get_image_length(request)
                file_header = 'HTTP/1.1 200 OK\r\nContent-Type: image/png\r\nContent-Length: ' + image_length + '\r\n\r\n'
            elif '.apng' in request:
                image_length = get_image_length(request)
                file_header = 'HTTP/1.1 200 OK\r\nContent-Type: image/apng\r\nContent-Length: ' + image_length + '\r\n\r\n'
            else:
                # Doesn't send a header type if not extension not listed. In many cases the file will still load - but you may be better to look up the MIME type for the file and add to the above list
                file_header = 'HTTP/1.1 200 OK\r\n'
            
            

            #print(request)
            
            #request = str(request)
            led_on = request.find("?led=on")
            led_off = request.find("?led=off")
            
            #stateis = ""
            if led_on > -1:
                print("Led is on")
                yellow_led.on()
                stateis = "LED is ON"
                
            if led_off > -1:
                print("Led is off")
                yellow_led.off()
                stateis = "LED is OFF"
            
            #response = html % stateis
            
            #response = html
            # sends back the content type of the file where known, together with content length if an image
            print(f"File header = {file_header}")
            cl.send(file_header)
            
            #runs the requested file through the open bit at the top of the code to get the file contents
            response = get_request_file(request)
            print(f"Response = {response}")
            
            # Send the content back
            cl.send(response)
            # Finish up
            cl.close()
            
            #
            
        except OSError as e:
            cl.close()
            print("Connection closed")
            
            

# Run the webpage loop
webpage_loop()

# Kill the socket when done
#s.close()

def disconnect_network():
    wlan.disconnect()
    
