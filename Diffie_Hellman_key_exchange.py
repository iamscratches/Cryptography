# -*- coding: utf-8 -*-
"""
Created on Sun May 23 19:13:16 2021

@author: subhankar
"""

'''
P: Prime number
G: G<P & G is primitive root of P

Key generation:-
    XA: XA<P                    -> private key
    YA: YA = G^(XA) mod P       -> public key
    
    XB: XB<P                    -> private key
    YB: YB = G^(XB) mod P       -> public key
    
secret key of:-
    A: k = (YB)^XA mod P
    B: k = (YA)^XB mod P
    
note: kA will be exactly equal to kB
    
'''

import sympy
import random
from math import sqrt


def generatePrime():    
    return sympy.randprime(20000, 2000000)


""" Iterative Function to calculate (x^n)%p
	in O(logy) */"""
def power( x, y, p):

	res = 1 
	x = x % p

	while (y > 0):
		if (y & 1):
			res = (res * x) % p
		y = y >> 1 
		x = (x * x) % p

	return res

def findPrimefactors(s, n) :
	while (n % 2 == 0) :
		s.add(2)
		n = n // 2
	for i in range(3, int(sqrt(n)), 2):
		while (n % i == 0) :

			s.add(i)
			n = n // i
	if (n > 2) :
		s.add(n)
        
def findPrimitive(n):
    s = set()    
    if(not sympy.isprime(n)):
        return -1
    
    phi = n - 1
    findPrimefactors(s, phi)
    roots = []
    for r in range(2, phi + 1):
        flag = False
        for it in s:
            if (power(r, phi // it, n) == 1):
                flag = True
                break
            if (flag == False):
                roots.append(r)
    if(len(roots)>0):
        return roots
	# If no primitive root found
    return -1


def generate_key():
    P = generatePrime()
    print("Prime number:", P)
    G = random.choice(findPrimitive(P))
    print("Primitive root:", G)
    XA = random.randint(20000, P)
    YA = power(G,XA,P)
    print("private & public key of a:", XA, YA)
    XB = random.randint(20000, P)
    YB = power(G,XB,P)
    print("private & public key of b:", XB, YB)
    A = power(YB,XA,P)
    B = power(YA,XB,P)
    print("secret key of a & b:", A, B)

# generate_key()