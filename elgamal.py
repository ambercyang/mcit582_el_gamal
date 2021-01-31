#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random

systemRandom = random.SystemRandom()

def legendre(a, p):
	if p < 2:
		raise ValueError('p must be >=2')
	if (a == 0) or (a == 1):
		return a
	if a % 2 == 0:
		r = legendre(a // 2, p)
		if ((p * p - 1) % 16) != 0:
			r *= -1
	else:
		r = legendre(p % a, a)
		if a % 4 == 3 and p % 4 == 3:
			r *= -1
	return r


def is_prime(n):
	if n == 2 or n == 3:
		return True
	if n % 2 == 0 or n % 3 == 0:
		return False

	k = 100
	for i in range(k):
		a = random.SystemRandom().randint(2,n-1)
		x = legendre(a, n)
		y = pow(a, (n - 1) // 2, n)
		if (x == 0) or (y != x % n):
			return False
	return True


def mod_inverse(a, m) : 
    m0 = m 
    y = 0
    x = 1
  
    if (m == 1) : 
        return 0
  
    while (a > 1) : 
        # q is quotient 
        q = a // m 
        t = m 
        # m is remainder now, process 
        # same as Euclid's algo 
        m = a % m 
        a = t 
        t = y 
        # Update x and y 
        y = x - q * y 
        x = t 
    # Make x positive 
    if (x < 0) : 
        x = x + m0 
    return x 


# In[2]:


g = 25321345895768332771257247786437404272984744155894636127038681207247189667957449171961226135739614116406340160439814400032380517973486272960710314505123563
p = 6828144732546360450297517841472310756057157731570065622984016572233987059659608961237735675415560304788239300920363559226081234452256463967048694754906561


# In[7]:


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
    temp = pow(c2,1,p) * pow(mod_inverse(c1, p),sk,p)
    m = pow(temp,1,p)
    
    
    return m


# In[4]:


[pk,sk] = keygen()
print("this is pk, sk:",[pk,sk])


# In[8]:


m = 3
c = [c1,c2] = encrypt(pk,m)


# In[9]:


my_m = decrypt(sk,c)
print("this is decripted m:", my_m)


# In[ ]:




