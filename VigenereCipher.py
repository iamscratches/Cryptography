# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 13:10:23 2021

@author: subhankar
"""
ALPHABET = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def vigenere_encrypt(plain_text, key):
    plain_text = plain_text.upper()
    key = key.upper()
    
    cipher_text = ''
    key_index = 0
    
    for character in plain_text:
        if character in ALPHABET:
            index = (ALPHABET.find(character) + (ALPHABET.find(key[key_index])))%len(ALPHABET)
            cipher_text = cipher_text + ALPHABET[index]
            
            key_index = (key_index + 1)%len(key)
    
    return cipher_text

def vigenere_decrypt(cipher_text, key):
    plain_text = ''
    key_index = 0
    key = key.upper()
    
    for character in cipher_text:
        if character in ALPHABET:
            index = (ALPHABET.find(character) - (ALPHABET.find(key[key_index])))%len(ALPHABET)
            plain_text = plain_text + ALPHABET[index]
            
            key_index = (key_index + 1)%len(key)
    
    return plain_text

def vigenere_encryptv2(plain_text, key):    
    cipher_text = ''
    key_index = 0
    
    for character in plain_text:        
        index = (ord(character) + ord(key[key_index])) % 256
        cipher_text = cipher_text + chr(index)
        
        key_index = (key_index + 1)%len(key)
    
    return cipher_text

def vigenere_decryptv2(cipher_text, key):
    plain_text = ''
    key_index = 0
    
    for character in cipher_text:
        index = (ord(character) - ord(key[key_index])) % 256
        plain_text = plain_text + chr(index)
        
        key_index = (key_index + 1)%len(key)
    
    return plain_text