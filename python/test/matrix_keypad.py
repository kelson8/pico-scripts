import machine
import time

# https://docs.sunfounder.com/projects/euler-kit/en/latest/pyproject/py_keypad.html

characters = [["1","2","3","A"],["4","5","6","B"],["7","8","9","C"],["*","0","#","D"]]

pin = [0,1,2,3]
row = []
for i in range(4):
    row.append(None)
    row[i] = machine.Pin(pin[i], machine.Pin.OUT)

pin = [4,5,6,7]
col = []
for i in range(4):
    col.append(None)
    col[i] = machine.Pin(pin[i], machine.Pin.IN)

def readKey():
    key = []
    for i in range(4):
        row[i].high()
        for j in range(4):
            if(col[j].value() == 1):
                key.append(characters[i][j])
        row[i].low()
    if key == [] :
        return None
    else:
        return key

last_key = None
while True:
    current_key = readKey()
    if current_key == last_key:
        continue
    last_key = current_key
    # Why doesn't this print off?
    if current_key == "1":
        print("1 Pressed")
        
    elif current_key != None:
        print(current_key)
    time.sleep(0.1)
