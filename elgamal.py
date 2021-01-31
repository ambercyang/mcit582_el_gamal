#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from elgamal_util import mod_inverse
import random

from params import p
from params import g


def keygen():
    sk = 0
    pk = 0
    
    a = random.randint(1, p) 
    #h = g^a % p
    h = pow(g,a,p)
    
    sk = a
    pk = h
    
    return pk,sk

def encrypt(pk,m):
    c1 = 0
    c2 = 0
    q = (p-1)/2
    r = random.randint(1, q) 
    #[c1,c2] =[ g^r%p, h^r*m%p]
    [c1,c2] = [pow(g,r,p), pow(pk,r,p)*m%p]
    
    return [c1,c2]

def decrypt(sk,c):
    #sk = g^a mod p
    m = 0
    #a=sk
    #m = (c2/c1^a) % p = (c2 % p) * [(1/c1)^a % p] %p
    temp = pow(c[1],1,p) * pow(mod_inverse(c[0], p),sk,p)
    m = pow(temp,1,p)
    
    
    return m

