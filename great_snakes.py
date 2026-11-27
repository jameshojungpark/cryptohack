#!/usr/bin/env python3

import sys
import base64
from Crypto.Util.number import long_to_bytes

if sys.version_info.major == 2:
    print("You are running Python 2, which is no longer supported. Please update to Python 3.")


print("Here is your flag:")

# XOR decoding: each number is XORed with the key 0x32, then converted to its character
ords = [81, 64, 75, 66, 70, 93, 73, 72, 1, 92, 109, 2, 84, 109, 66, 75, 70, 90, 2, 92, 79]
print("".join(chr(o ^ 0x32) for o in ords))

# ASCII decoding: each number is an ASCII code, converted to its character with chr()
ascii_list = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
print("".join(chr(code) for code in ascii_list))

# Hex decoding: the hex string is turned into raw bytes, then decoded into text
hex = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"
print(bytes.fromhex(hex).decode())

# Base64 encoding: the hex string is turned into raw bytes, then those bytes are encoded as Base64
base_64 = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
print(base64.b64encode(bytes.fromhex(base_64)).decode())

# Integer decoding: the long integer is turned into raw bytes, then decode into text
big_integer = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
print(long_to_bytes(big_integer).decode())
