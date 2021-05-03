# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 18:17:31 2021

@author: subhankar
"""

from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import sys
BLOCK_SIZE = 64 # Bytes

# We can use the DES algorithm like this
# there are several modes (7 modes)
# 1.) ECB: "Electronic Code Block" -> We use DES on every 64bits long plain text block
#         these blocks are independent of each other so we can use DES separately on every block
# 2.) CBC: "Cipher Block Chaining" -> uses a chaining mechanism that causes
#         the decryption of a block of ciphertext to depend on all the preceeding cipher text blocks
        
#     THE PADDING PROBLEM
#         DES algorithm uses 64 bits long inputs: what if the plain text is not divisible by 64?
#             ~ in these cases we append some extra bits to the plain text to be able to split the plain text
#                 into 64 bits long chunks
        
#         Padding modes:
#             -> we can add extra bits: 1000000 for example
#             -> we can add white-spaces to the plain text
#             -> we can use CMS "Cryptographic Message Syntax"... pad with bytes all the same value as the number of padding bytes


def DESencrypt(plain_text, key):
    
    cipher = DES.new(key.encode('utf8'), DES.MODE_ECB)
    cipher_text = cipher.encrypt(pad(plain_text.encode('utf8'), BLOCK_SIZE))
    return cipher_text

def DESdecrypt(cipher_text, key):
    decipher = DES.new(key.encode('utf8'), DES.MODE_ECB)
    msg_dec = decipher.decrypt(cipher_text)
    return unpad(msg_dec, BLOCK_SIZE)











































