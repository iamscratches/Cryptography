# -*- coding: utf-8 -*-
"""
Created on Mon May  3 20:02:39 2021

@author: subhankar
"""

"""
Plain text block : 128bits(4 words becoz 1 word is 32 bits)
key size : 128bits(4 words)
number of subkeys : 10 subkeys
number of rounds : 10 rounds(or 12 or 14)
    In each round we use 1 subkey + we have to use the original
    128 bits long key before applying the round-function
ciphertext block : 128 bits
"""
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
BLOCK_SIZE = 128 # Bytes

def AESencrypt(plain_text, key):
    
    cipher = AES.new(key, AES.MODE_ECB)
    cipher_text = cipher.encrypt(pad(plain_text.encode('utf8'), BLOCK_SIZE))
    return cipher_text

def AESdecrypt(cipher_text, key):
    decipher = AES.new(key, AES.MODE_ECB)
    msg_dec = decipher.decrypt(cipher_text)
    return unpad(msg_dec, BLOCK_SIZE)
