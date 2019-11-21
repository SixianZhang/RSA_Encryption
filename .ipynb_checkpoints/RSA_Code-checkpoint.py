import random
import numpy as np
# import matplotlib.pyplot as plt
# from IPython.core.debugger import set_trace

# ## Key generation
def random_prime(d = 32, mode = 'MR', k = 10):
    # generate a large prime number randomly
    # Simple method
    # Consider Miller–Rabin and Solovay–Strassen primality test
    
    
    
    n = random.randint(2, 2**d - 1)
    
    # Preliminary Test
    while n % 2 == 0 or n < 3:
        n = random.randint(2, 2**d - 1)
    
    # Iterative Test
    if mode == 'simple':
        while not simple_primality_test(n):
            n += 2
    elif mode == 'MR':
        while not MR_primality_test(n, k):
            n += 2

    return n

def simple_primality_test(n:int):
    # Iterative Test
    while n % 2 == 0 or n % 3 == 0 or n < 3 == 0:
        return False
    
    i = 5
    while i*i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True

def MR_primality_test(n:int, k:int):
    
    if n <= 1:
        return False
    
    if n < 4:
        return True
    
    if n & 1 == 0:
        return False
    
    d = n - 1
    r = 0
    
    while d & 1 == 0:
        r += 1
        d = d >> 1
    
    for i in range(0, k):
        keep_loop = False
        a = random.randint(2, n-2)
        x = fast_expontiation(a, d, n)
        
        if x == 1 or x == n - 1:
            continue
            
        for j in range(0, r - 1):
            x = x**2 % n
            if x == n - 1:
                keep_loop = True
                break
        
        if keep_loop:
            continue
        else:
            return False
    return True

def gcd(x, y):
    if x < y:
        x, y = y, x
    
    while not x - y == 0:
        x = x - y
        if x < y:
            x, y = y, x        
    
    return x  

def random_coprime(n):
    # find e, which satisfies gcd(n, e) = 1. 1 < e < n
    
    # Can't do this, memory overflow
    #e_seq = np.random.permutation(np.arange(2, n))
        
    e = random.randint(2, n - 1)
    
    while not gcd(n, e) == 1:
        if e == n - 1:
            e = random.random.randint(2, n -1)
        else:
            e = e + 1
        
    return e


def eea(r0, r1):
    # find the inverse of e under the modular base phi_n
    if r0 < r1:
        r0, r1 = r1, r0
    
    if r1 == 1:
        return 1
    
    if r0 % r1 == 0:
        return None
    
    n = r0
    
    s0 = 1; t0 = 0; s1 = 0; t1 = 1   
    q0 = 0; q1 = int(r0 / r1)
    
    while True:
        r2 = r0 % r1
        q2 = int(r1 / r2)
        s2 = s0 - q1*s1
        t2 = t0 - q1*t1

        if r2 == 1:
            if t2 < 0: 
                return t2 + n
            else:
                return t2
        else:
            r0 = r1; q0 = q1; s0 = s1; t0 = t1
            r1 = r2; q1 = q2; s1 = s2; t1 = t2

def key_generation(d = 32):
    p = random_prime(d)
    q = random_prime(d)

    while p == q:
        q = random_prime(d)

    n = p * q
    phi_n = ( p - 1 )*(q - 1)

    e = random_coprime(phi_n)

    d = eea(e, phi_n)
    
    return p, q, n, phi_n, e, d

# ## Encryption

def fast_expontiation(base:int, power:int, n = 1):
    # Calculating base^power mod n
#     if type(key) is int:
    power_seq = int_to_list(power)
    
    answer = base
    
    for i in range(1, len(power_seq)):
        answer = (answer ** 2) % n
        if power_seq[i] == 1:
            answer = (answer * base) % n
 
    return answer

def int_to_list(n:int):
    lst = []

    while n > 0:
        lst.append(n & 1)
        n = n >> 1
    
    lst.reverse()
    
    return lst
    
def list_to_int(lst:list):
    n = 0
    
    lst.reverse()
    
    for i in range(0, len(lst)):
        n = n + lst[i] * (2**i)
    
    return n

def encryption(plain_text, n, key):
    
#     cipher = (plain_text ** key) % n
    
    exponent = fast_expontiation(plain_text, key, n)    
    cipher = exponent % n
    
    return cipher


# ## Decryption

def decryption(cipher, n, key):
    
#     plain_text = (cipher ** key) % n

    exponent = fast_expontiation(cipher, key, n)    
    plain_text = exponent % n
    
    return plain_text

def decryption_CRT(cipher, p, q, d):
    
    plain_text = chinese_remainder_theorem(cipher, p, q, d)
    
    return plain_text

def chinese_remainder_theorem(C, p, q, d):
    # realize CRT algorithm
    
    dp = d % (p-1)
    dq = d % (q-1)
    Cp = C % p
    Cq = C % q
    
    a1 = fast_expontiation(Cp, dp, p)
    a2 = fast_expontiation(Cq, dq, q)
    
    qp = eea(q % p, p)
    pq = eea(p % q, q)
    
    P = (a1*q*qp + a2* p* pq) % (p * q)
    
    return P

def str_to_list(string: str):
    
    lst = []
    
    for s in string:
        lst.append(int.from_bytes(s.encode('utf-8'), 'big'))
    
    return lst

def main():
  
    # Input key length
    while True:
        try:
            key_length = int(input("Please enter the length of the key: "))
            if key_length > 1024:
                print("The maximum length for this program is currently 1024. Use 1024 instead.")
                key_length = 1024
            break
        except ValueError:
            print("Key length has to be an integer")
            continue


        
    # Key generation
    p, q, n, phi_n, e, d = key_generation(key_length)

    # Plain text
    plain_text_raw = str(input("Please enter the plain text: "))
    
    plain_text = str_to_list(plain_text_raw)
    
    # Encryption
    cipher = []
    for element in plain_text:
        cipher.append(encryption(element, n, e))

    print("The plain text is: " + str(plain_text_raw))
    print("The cipher is :" + str(cipher))

    # Decryption
    decrpt_text = []
    for element in cipher:
        decrpt_text.append(decryption(element, n, d))

    print("The decrypted text is: " + str(bytes(decrpt_text).decode('utf-8')))

    # Decrytion CRT
    decrpt_text_crt = []
    for element in cipher:
        decrpt_text_crt.append(decryption_CRT(element, p, q, d))

    print("The decrypted text using CRT is: " + str(bytes(decrpt_text_crt).decode('utf-8')))
    
if __name__ == "__main__":
    main()

