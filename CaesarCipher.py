import sys
import matplotlib.pylab as plt

ALPHABET = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# We will store all the english words in a list
ENGLISH_WORDS = []

# load the english words
def getData():
    dictionary = open("words.txt","r")
    for word in dictionary.read().split("\n"):
        ENGLISH_WORDS.append(word.upper())
        
    dictionary.close()
    
# count the number of english words in a given text
def count_words(text):
    text = text.upper()
    words = text.split(' ')
    matches = 0
    
    for word in words:
        if word in ENGLISH_WORDS:
            matches += 1
            
    return matches

# decides whether a given text is english or not
def is_text_english(text):
    getData()    
    matches = count_words(text)
    if(( float(matches) / len(text.split(" ")) * 100 ) >= 70):
        print(matches)
        return True
    return False

#caeser encryption algorithm
def caeser_encrypt(plain_text, KEY=15):

    #the encrypted message
    cipher_text = ''

    #make all the plain text in upper case so that it's case insensetive
    plain_text = plain_text.upper()

    for c in plain_text:
        if c in ALPHABET:
            index = ALPHABET.find(c)
    
            index = (index + KEY)%len(ALPHABET)
    
            cipher_text = cipher_text + ALPHABET[index]

    return cipher_text


def caeser_decrypt(cipher_text, KEY=3):

    #decrypted text message
    plain_text = ''

    for c in cipher_text:
        index = ALPHABET.find(c)

        index = (index - KEY)%len(ALPHABET)

        plain_text = plain_text + ALPHABET[index]

    return plain_text

def caeser_encryptv2(plain_text,KEY=3):
    cipher_text=''
    for c in plain_text:
        index = ord(c)
        index = (index+KEY)%256
        cipher_text = cipher_text + chr(index)

    return cipher_text;

def caeser_decryptv2(plain_text,KEY=3):
    cipher_text=''
    for c in plain_text:
        index = ord(c)
        index = (index-KEY)%256
        cipher_text = cipher_text + chr(index)

    return cipher_text;

def caeser_crack(cipher_text):
    for key in range(len(ALPHABET)):
        plain_text = ''

        for c in cipher_text:
            index = ALPHABET.find(c)
            index = (index - key)%len(ALPHABET)
            plain_text = plain_text + ALPHABET[index]

        print('with key %s, the result is: %s'%(key, plain_text))
        if(is_text_english(plain_text)):
            print('The key is %s and the decrypted text is : %s'%(key, plain_text))
            return
        

def frequency_analysis(plain_text):
    letter_frequency = {}
    plain_text = plain_text.upper()    
    
    for letter in range(0,len(ALPHABET)):
        letter_frequency[ALPHABET[letter]] = 0
    
    for letter in plain_text:
        if letter in ALPHABET:
            letter_frequency[letter] += 1
        
    return letter_frequency

def plot_distribution(letter_frequency):
    centers = range(len(ALPHABET))
    plt.bar(centers, letter_frequency.values(), align='center', tick_label=letter_frequency.keys())
    plt.xlim([0, len(ALPHABET)])
    plt.show()

'''       
if __name__ == '__main__':
    input_text = input("Enter plain text : ")
    print("Encrypted Text : " + caeser_encryptv2(input_text,15))
    print("Decrypted Text : " + caeser_decryptv2(caeser_encryptv2(input_text,15),15))
'''

    
    
