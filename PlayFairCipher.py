# -*- coding: utf-8 -*-
"""
Created on Sat May 15 11:44:28 2021

@author: subhankar
"""

'''
1. Repeating the plain letters in the same pair must be separated 
with a filler letter X.
2. If the plain text has an odd number of characters add an X to
the end to make it even.
3. Two plain text letter that fall in the same row of the matrix are
each replaced by the letter to the right with the first element of the
row circularly following the last.
4. Two plain text letter that fall in the same column are each 
replaced by the letter beneath with the top element of the column 
circularly following the last.
5. Otherwise each plain text letter in a pair is replaced by the 
letter that lies in its own row and the column occupied by the other 
plain text letter.
'''

def plain_fair_encrypt(plain_text, key):
    keyset = set(key.upper())
    plain_text = plain_text.upper()
    table = []
    k=len(keyset)
    
    for i in keyset:
        table.append(i)
    
    for i in range(65, 91):
        if(chr(i) not in keyset):
            if(k!=25):                    
                table.append(chr(i))
                k += 1
            else:
                table[24] += chr(i)
                
    plain_text = list(plain_text)
    
    string = ""
    for i in range(len(plain_text) - 1 ):
        string += plain_text[i]
        if(plain_text[i] == plain_text[i+1]):
            string += 'X'
    string += plain_text[len(plain_text) - 1]
    plain_text = string
    
    if len(plain_text)%2 !=0:
        plain_text += 'X'
               
        
    broken_text = []
    i = 0
    
    while i < len(plain_text):
        broken_text.append(plain_text[i:i+2])
        i += 2
    
    cipher_text = ""
    # print(table)
    # print(broken_text)
    for block in broken_text:
        block = list(block)
        try:
            index1 = table.index(block[0])        
        except:
            index1 = 24
        try:
            index2 = table.index(block[1])
        except:
            index2 = 24
        row1 = int(index1%5)
        col1 = int(index1/5)
        row2 = int(index2%5)
        col2 = int(index2/5)
        if(row1==row2):
            # print("row", block, (row1,col1), (row2, col2))
            cipher_text += table[(col1*5 + row1 + 5)%25] + table[(col2*5 + row2 + 5)%25]
        elif(col1==col2):
            # print("col", block, (row1,col1), (row2, col2))
            cipher_text += table[(row1+1)%25] + table[(row2+1)%25]        
        else:
            # print("none", block, (row1,col1), (row2, col2))
            cipher_text += table[(col2*5 + row1)%25] + table[(col1*5 + row2)%25]
        # print(cipher_text)
    return cipher_text

print(plain_fair_encrypt("thisisasecretmessagethatneedstobeencrypted", "secretkey"))
