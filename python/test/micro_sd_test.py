import machine
import sdcard
import uos

# This works now!
# I needed to use 5v for this, I read the reviews of it on amazon
# I am using this kit: https://www.amazon.com/dp/B07MTTLF75

# Extra info:
"""
    https://www.digikey.com/en/maker/projects/raspberry-pi-pico-rp2040-sd-card-example-with-micropython-and-cc/e472c7f578734bfd96d437e68e670050
    https://medium.com/@marcj_40686/using-an-sd-card-with-the-raspberry-pi-pico-for-data-storage-in-micropython-da9c8264c04c
    https://microcontrollerslab.com/micro-sd-card-module-raspberry-pi-pico/
    
"""

"""
    
"""

# Assign chip select (CS) pin (and start it high)
cs = machine.Pin(9, machine.Pin.OUT) # GP9 (Pin 12)

# Intialize SPI peripheral (start with 1 MHz)
spi = machine.SPI(1,
                  baudrate=1000000, # 1 MHz
                  polarity=0,
                  phase=0,
                  bits=8,
                  firstbit=machine.SPI.MSB,
                  sck=machine.Pin(10), # GP10 (Pin 14)
                  mosi=machine.Pin(11), # GP11 (Pin 15)
                  miso=machine.Pin(8)) # GP8 (Pin 11)

# Initialize SD card
sd = sdcard.SDCard(spi, cs)

# Mount filesystem
vfs = uos.VfsFat(sd)
uos.mount(vfs, "/sd")

def write_to_card(file, text):
    with open(f"/sd/{file}.txt", "w") as f:
        f.write(text)
    
    print("Success")

def read_from_card(file):
    with open(f"/sd/{file}.txt", "r") as f:
        data = f.read()
        print(data)
        
        
file_name = "test"
file_text = """
Hello world
This should be a multiline string on the sd card
Can you see it?
"""
write_to_card(file_name, file_text)
read_from_card(file_name)

#####
# Old code

# Create a file and write something to it
#with open("/sd/test01.txt", "w") as file:
#    file.write("Hello, SD World!\r\n")
#    file.write("This is a test\r\n")

# Open the file we just created and read from it
#with open("/sd/test01.txt", "r") as file:
#    data = file.read()
#    print(data)
#####
