# Cryptography
'''Here is how this project works'''
- First let me show around how this project structure is maintained.
- We save the file that needs to be encrypted in the files folder
- The encrypted_files folder contains all the encrypted files that gets saves after encryprion.
- The decrypted_files folder contains all the decrypted files that gets saved after decryption.
- We can either generate a new key for encryption or use an existing key for encryption and also check whether the decrypted and original files are equal or not

This encryption algorithm uses levels that we can choose in order to determine the level of encryption we want to put in on our file to prevent it from information leaking.
#Note: Remember the more the level of encryption the greater the time it will take to encrypt the file.
For files that are generally of low size like text files etc. we can use higher level of encryption but for higher file size especially image & video files doesn't need much high level of
encryption as it becomes harder to crack such files with even small level of encryptions
