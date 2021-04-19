# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 14:36:59 2021

@author: subhankar
"""

from random import randint
import matplotlib.pylab as plt

ALPHABET = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
key = []

def oneTimePad_encrypt(plain_text):
    plain_text = plain_text.upper()
    cipher_text = ''
    random_sequence(plain_text)
    
    for index, char in enumerate(plain_text):
        if char in ALPHABET:
            key_index = key[index]
            char_index = ALPHABET.find(char)
            cipher_text += ALPHABET[(char_index + key_index)%len(ALPHABET)]
    
    return cipher_text
    
def oneTimePad_decrypt(cipher_text):
    cipher_text = cipher_text.upper()
    plain_text = ''
    
    for index, char in enumerate(cipher_text):
        key_index = key[index]
        char_index = ALPHABET.find(char)
        plain_text += ALPHABET[(char_index - key_index)%len(ALPHABET)]
    
    return plain_text

def random_sequence(plain_text):
    
    # we store the random values in a list
    random_sequence = []
    global key
    # generating as many random values as the number of characters in the plain text
    # size of the key = size of the plain text
    for rand in range(len(plain_text)):
        random_sequence.append(randint(0, len(ALPHABET)))
    key = random_sequence
    

def oneTimePad_frequency_analysis(plain_text):
    letter_frequency = {}
    plain_text = plain_text.upper()    
    
    for letter in range(0,len(ALPHABET)):
        letter_frequency[ALPHABET[letter]] = 0
    
    for letter in plain_text:
        if letter in ALPHABET:
            letter_frequency[letter] += 1
        
    return letter_frequency

def oneTimePad_plot_distribution(letter_frequency):
    centers = range(len(ALPHABET))
    plt.bar(centers, letter_frequency.values(), align='center', tick_label=letter_frequency.keys())
    plt.xlim([0, len(ALPHABET)])
    plt.show()