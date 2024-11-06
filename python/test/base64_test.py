import base64
import sys

import os

# Copied from my test projects

def encode(text):
    test_string_bytes = text.encode("ascii")

    base64_bytes = base64.b64encode(test_string_bytes)
    base64_string = base64_bytes.decode("ascii")
    return base64_string
    
def decode(text):
    base64_bytes = text.encode("ascii")

    text_string_bytes = base64.b64decode(base64_bytes)
    text_string = text_string_bytes.decode("ascii")

    return text_string

test_string = "It works!"

def write_to_file(file):
    text_file = file + ".txt"

    base64_string = "SXQgd29ya3Mh"
    file = open(text_file, "w")
    base64_encoded = encode(test_string)
    base64_decoded = decode(base64_string)
    
    file.write(f"Encoded string: {base64_encoded}\n")
    file.write(f"Decoded string: {base64_decoded}")
    file.close()
    
    print("Wrote text to file")
    
write_to_file("test")


#print(os.listdir("/"))
 

#print(f'Encoded string: {encode(test_string)}')

#print(f"Decoded string: {decode("SSBEb24ndCBDYXJl")}")
