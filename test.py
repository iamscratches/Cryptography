from CaesarCipher import *
from VigenereCipher import *
from OneTimePad import *
input_text = input("Enter plain text : ")
# print("Encrypted Text : " + caeser_encryptv2(input_text,15))
# print("Decrypted Text : " + caeser_decryptv2(caeser_encryptv2(input_text,15),15))

# print("Encrypted Text : " + caeser_encrypt(input_text,15))
# caeser_crack(caeser_encrypt(input_text,15))
# plot_distribution(frequency_analysis(input_text))
# plot_distribution(frequency_analysis(caeser_encrypt(input_text)))
# input_key = input("Enter secret key : ")
# encrypted_text = vigenere_encrypt(input_text, input_key)
# decrypted_text = vigenere_decrypt(encrypted_text, input_key)
# print("Encrypted text : " + encrypted_text)
# print("Decryted text : " + decrypted_text)

# encrypted_text = vigenere_encryptv2(input_text, input_key)
# decrypted_text = vigenere_decryptv2(encrypted_text, input_key)
# print("Encrypted text : " + encrypted_text)
# print("Decryted text : " + decrypted_text)

cipher_text = oneTimePad_encrypt(input_text)
print("Encrypted Text : " + cipher_text)
print("Decrypted Text : "+ oneTimePad_decrypt(cipher_text))
plot_distribution(frequency_analysis(input_text))
plot_distribution(frequency_analysis(cipher_text))