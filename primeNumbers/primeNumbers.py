import math
import time

def is_prime_v1(n):
    """Return 'True' if 'n' is a prime number. False otherwise."""
    if n == 1:
        return False # n is not considered prime, so function must return false

    for d in range(2, n):
        if n % d == 0:
            return False
    return True

def is_prime_v2(n):
    """Return 'True' if 'n' is a prime number. False otherwise."""
    if n == 1:
        return False # n is not considered prime, so function must return false
    
    max_divisor = math.floor(math.sqrt(n))
    for d in range(2, 1 + max_divisor):
        if n % d == 0:
            return False
    return True

def is_prime_v3(n):
    """Return 'True' if 'n' is a prime number. False otherwise."""
    if n == 1:
        return False # n is not considered prime, so function must return false
    
    # If n is even and not 2, then it isn't prime
    if n == 2:
        return True
    if n > 2 and n % 2 == 0:
        return False
    
    max_divisor = math.floor(math.sqrt(n))
    for d in range(3, 1 + max_divisor, 2):
        if n % d == 0:
            return False
    return True

# -=-=-= Test Function =-=-=- #
#for n in range(1, 21):
#    print(n, is_prime_v2(n))
       
# -=-=-= Time Function =-=-=- #
t0 = time.time()
for n in range(1, 100000):
    is_prime_v1(n)
t1 = time.time()
print("Time to process v1: ", t1-t0)
for n in range(1, 100000):
    is_prime_v2(n)
t2 = time.time()
print("Time to process v2: ", t2-t1)
for n in range(1, 100000):
    is_prime_v3(n)
t3 = time.time()
print("Time to process v3: ", t3-t2)
