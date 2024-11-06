#              .';:cc;.
#            .,',;lol::c.
#            ;';lddddlclo
#            lcloxxoddodxdool:,.
#            cxdddxdodxdkOkkkkkkkd:.
#          .ldxkkOOOOkkOO000Okkxkkkkx:.
#        .lddxkkOkOOO0OOO0000Okxxxxkkkk:
#       'ooddkkkxxkO0000KK00Okxdoodxkkkko
#      .ooodxkkxxxOO000kkkO0KOxolooxkkxxkl
#      lolodxkkxxkOx,.      .lkdolodkkxxxO.
#      doloodxkkkOk           ....   .,cxO;
#      ddoodddxkkkk:         ,oxxxkOdc'..o'
#      :kdddxxxxd,  ,lolccldxxxkkOOOkkkko,
#       lOkxkkk;  :xkkkkkkkkOOO000OOkkOOk.
#        ;00Ok' 'O000OO0000000000OOOO0Od.
#         .l0l.;OOO000000OOOOOO000000x,
#            .'OKKKK00000000000000kc.
#               .:ox0KKKKKKK0kdc,.
#                      ...
#
# Author: peppe8o
# Blog: https://peppe8o.com
# Date: Aug 26th, 2021
# Version: 1.0

from machine import Pin
import utime
import random

dataPIN = 19
latchPIN = 18
clockPIN = 17

dataPIN=Pin(dataPIN, Pin.OUT)
latchPIN=Pin(latchPIN, Pin.OUT)
clockPIN=Pin(clockPIN, Pin.OUT)

def shift_update(input,data,clock,latch):
  #put latch down to start data sending
  clock.value(0)
  latch.value(0)
  clock.value(1)
  
  #load data in reverse order
  for i in range(7, -1, -1):
    clock.value(0)
    data.value(int(input[i]))
    clock.value(1)

  #put latch up to store data on register
  clock.value(0)
  latch.value(1)
  clock.value(1)
  
#main program, calling shift register function
bit_string="00000000"

while True:
    shift_update(bit_string,dataPIN,clockPIN,latchPIN)
    bit_string = str(random.randint(0, 1))+bit_string[:-1]
    utime.sleep(0.3)