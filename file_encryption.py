# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 11:26:40 2021

@author: subhankar
"""
from RSA2 import *
import time
#       ENCRYPTION

def encrypt_file(filename):
    file = open("files/" + filename, "rb")
    encrypted_file = open("encrypted_files/encrypted_" + filename, "wb")
    
    read_by = 16        # read 64 bytes of data from the file one by one
    byte = file.read(read_by)
    
    while byte:
        encrypted_data = RSAencrypt(byte)
        # print(len(encrypted_data))
        for data in encrypted_data:
            encrypted_file.write(data)    
        byte = file.read(read_by)
    encrypted_file.close()
    file.close()
    
    print("encryption done.\nFile is saved in location:")
    print("encrypted_files/encrypted_" + filename)
    return "encrypted_" + filename
    

#       DECRYPTION

def decrypt_file(filename):
    encrypted_file = open("encrypted_files/" + filename, "rb")
    decrypted_file = open("decrypted_files/de_" + filename, "wb")   
    
    byte = encrypted_file.read(4)
    
    while byte:
        decrypted_data = RSAdecrypt(byte)
        # for data in decrypted_data:
        decrypted_file.write(decrypted_data)
        # print(type(decrypted_data),decrypted_data)
        byte = encrypted_file.read(4)    
    encrypted_file.close()
    decrypted_file.close()
    
    print("decryption done.\nFile is saved in location:")
    print("decrypted_files/de_" + filename)
    return "de_" + filename


#       CHECK FOR FILE CONVERSION ERRORS

def check_files(path1, path2):
    file = open(path1, "rb")
    decrypted_file = open(path2, "rb")
    file_read = file.read()
    decrypted_file_read = decrypted_file.read()
    if(file_read == decrypted_file_read):
        print("It's equal")
    else:
        print("It's not equal")
        
    file.close()
    decrypted_file.close()

start_time = time.time()
encrypted_filename = encrypt_file("image.jpg")
decrypted_filename = decrypt_file(encrypted_filename)
check_files("files/text.txt","decrypted_files/" + decrypted_filename)
print(f'execution completes in {(time.time() - start_time)} seconds')