from mfrc522 import SimpleMFRC522
import utime

# https://docs.sunfounder.com/projects/euler-kit/en/latest/pyproject/py_rfid.html

from picozero import LED

reader = SimpleMFRC522(spi_id=0,sck=6,miso=4,mosi=7,cs=5,rst=22)
yellow = LED(18)

# Sleep time in ms
sleep_time = 1000

def read():
    print("Reading, please place the card")
    id, text = reader.read()
    print(f"ID: {id}\nText: {text}")
    
def read_id():
    print("Reading, please place the card\n")
    id = reader.read_id()
    
    if id == 122730500882:
        print("Authorized\n")
        # Oops I had this set to sleep instead of sleep_ms, I think it was trying to sleep for 500 seconds lol.
        yellow.on()
        utime.sleep_ms(500)
        yellow.off()
    else:
        print("You do not have permission!\n")
    
    #print(f"ID: {id}")
    
    
def main_loop():
    while True:
        read_id()
        utime.sleep_ms(sleep_time)
        
if __name__ == '__main__':
    try:
        main_loop()
    except KeyboardInterrupt:
        print("Exiting")
