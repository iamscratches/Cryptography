# -*- coding: utf-8 -*-
"""
Created on Sun May 16 20:32:20 2021

@author: subhankar
"""

'''
1. Calculate two large prime numbers P and Q
2. Calculate n = P*Q
3. Calculate fi(n) = (P-1)(Q-1)
4. Assume e such that gcd(e, fi(n)) = 1 and 1<e<fi(n)
5. Assume d such that d = e^(-1) mod fi(n)
                    =>d*e mod fi(n) = 1 mod fi(n)
                    =>d*e mod fi(n) = 1
6. Public key = {e, n}
7. Private key = {d, n}
8. For encryption, c = (M^e)mode n
8. For decryption, M = (c^e)mode n
'''

import sympy

def generateKey():    
    return sympy.randprime(200, 20000),sympy.randprime(200, 20000)

def generatePair():
    i = 1
    while(True):        
        print("checkpoint 2", (fi*i+1))
        factors = get_factors(fi*i+1)
        print("checkpoint 3", factors)
        i += 1
        if(len(factors)>4):
            break
        
    print("checkpoint 4 final", factors)
    E = factors[int(len(factors)/2-1)]
    D = factors[int(len(factors)/2)]
    print("checkpoint 5 final", E, D)
    if(E<=1 or E>=fi):
        print("failed")
        return [0,0]
    else:
        return E,D

def get_factors(x):
   factors = []
   for i in range(1, x + 1):
       if x % i == 0:
           factors.append(i)
   return factors

generatedPrime = generateKey()
P=generatedPrime[0]
Q=generatedPrime[1]
n = P*Q
fi = (P-1)*(Q-1)

print("checkpoint 1", P, Q, fi-1, n)

# choose a value for e
# d * e = 1 mod fi => d * 7 = 1 mod 20
l = generatePair()
print("checkpoint 5", l)
e = l[0]
d = l[1]
if((e*d)%fi==1):
    print("checkpoint 6", "successful", e, d)    

public_key = [e,n]
private_key = [d,n]

def RSAencrypt(plain_text):
    plain_text = list(plain_text)
    cipher_text = []
    for i in plain_text:
        cipher_text.append((ord(i)**public_key[0])%public_key[1])
    return cipher_text

def RSAdecrypt(cipher_text):
    plain_text = []
    for i in cipher_text:
        plain_text.append(chr((i**private_key[0])%private_key[1]))
    plain_text = ''.join(plain_text)
    return plain_text


