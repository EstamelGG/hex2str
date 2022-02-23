#!/usr/bin/python3
def decrypt():
    hexinput = input("hex:")
    hexinput = hexinput.replace("\\x", "")
    bytes_obj = bytes.fromhex(hexinput)
    readable = bytes_obj.decode("ASCII")
    print(readable)


while 1:
    decrypt()
