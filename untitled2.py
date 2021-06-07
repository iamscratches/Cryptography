# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 13:48:14 2021

@author: subhankar
"""
# from RSA2 import *

# def count_words(filepath):
#    with open(filepath) as f:
#        print(type(f.read()))
#        data = f.read()
#        data.replace(",", " ")
#        return len(data.split(" "))
# # print(count_words("hello.txt"))

# my_file = open("test_file.txt", "w")
# string_list = ["HEllo", "World"]
# my_file.write("First Line\n")
# my_file.write("Second Line")
# my_file = open("test_file.txt")
# content = my_file.read()
# my_file.close()
# print(content)

# file = open("135625.jpg", "rb")
# take = 64
# byte = file.read(take)
# # print(list(byte))
# print(byte)
# list_byte = list(byte)
# print(list_byte)
# print(list_byte[1].to_bytes(1,'big'))
# integer_val = int.from_bytes(byte, "big",)
# print(integer_val)
# # while byte:
# #     print(int.from_bytes(byte, "big",))
# #     byte = file.read(1)

# byte_val = integer_val.to_bytes(take, 'big')
# print(byte_val)
# if(byte_val == byte):
#     print("Equal")

# integer = int.from_bytes(byte_val, "big",)
# if(integer_val == integer):
#     print("Equal")
# my_file = open("test_file.txt", "w")
# my_file.write("First Line\n")
# my_file.write("Second Line")
# my_file.close()


#       ENCRYPTION

# file = open("download.png", "rb")
# encrypted_file = open("test_file6.png", "wb")

# read_by = 16        # read 64 bytes of data from the file one by one
# byte = file.read(read_by)

# while byte:
#     encrypted_data = RSAencrypt(byte)
#     # print(len(encrypted_data))
#     for data in encrypted_data:
#         encrypted_file.write(data)    
#     byte = file.read(read_by)
# encrypted_file.close()
# file.close()

# print("encryption done.")

# #       DECRYPTION

# encrypted_file = open("test_file6.png", "rb")
# decrypted_file = open("test_file7.png", "wb")



# byte = encrypted_file.read(4)

# while byte:
#     decrypted_data = RSAdecrypt(byte)
#     # for data in decrypted_data:
#     decrypted_file.write(decrypted_data)
#     # print(type(decrypted_data),decrypted_data)
#     byte = encrypted_file.read(4)

# print("done!")
# encrypted_file.close()
# decrypted_file.close()

# file = open("hello.txt", "rb")
# decrypted_file = open("test_file7.txt", "rb")
# file_read = file.read()
# decrypted_file_read = decrypted_file.read()
# if(file_read == decrypted_file_read):
#     print("It's equal")
# else:
#     print("It's not equal")
    
# file.close()
# decrypted_file.close()




# file = open("files/text.txt", "rb")
# encrypted_file = open("encrypted_files/encrypted_text.txt", "rb")
# # file_read = file.read(4)
# encrypted_file_read = encrypted_file.read(64)
# # print(list(file_read))
# # print(encrypted_file_read)
# # k = int.from_bytes(encrypted_file_read, "little")
# # print(k)
# # enlist = list(encrypted_file_read)
# # i = 0
# # enlist_convert = []
# # # print(len(enlist))
# # while(i<len(enlist)):    
# #     enlist_convert.append(bytes(bytearray(enlist[i:i+4])))
# #     i += 4
    
# # print(enlist_convert)
# # print(RSAdecrypt(encrypted_file_read))
# # for en in enlist_convert:
# #     print(RSAdecrypt(en), end=" ")
# print(RSAdecrypt2(encrypted_file_read))
# # print(RSAdecrypt(enlist_convert))
# # file.close()
# encrypted_file.close()

# import os
# # get the size of file
# size = os.path.getsize('files/text.txt') 
# print('Size of file is', size, 'bytes')

# txt = "Hello\rWorld!"
# print(txt) 

import time
for i in range(100):
    print('\r',i, end="%")
    time.sleep(0.01)