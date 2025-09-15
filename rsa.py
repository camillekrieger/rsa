import random
import sys
from fermat import miller_rabin

# If you use a recursive implementation of `mod_exp` or extended-euclid,
# you recurse once for every bit in the number.
# If your number is more than 1000 bits, you'll exceed python's recursion limit.
sys.setrecursionlimit(4000)

# When trying to find a relatively prime e for (p-1) * (q-1)
# use this list of 25 primes
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

def ext_euclid(a: int, b: int) -> tuple[int, int, int]:
    """
    The Extended Euclid algorithm
    Returns x, y , d such that:
    - d = GCD(a, b)
    - ax + by = d

    Note: a must be greater than b
    """
    if b == 0:
        return 1, 0, a
    x, y, z = ext_euclid(b, a % b)
    return y, x - ((a//b)*y), z

def generate_large_prime(bits=512) -> int:
    """
    Generate a random prime number with the specified bit length.
    Use random.getrandbits(bits) to generate a random number of the
     specified bit length.
    """
    x = random.getrandbits(bits)
    while miller_rabin(x, 100) == 'composite':
        x = random.getrandbits(bits)
    return x  # Guaranteed random prime number obtained through fair dice roll

def generate_key_pairs(bits: int) -> tuple[int, int, int]:
    """
    Generate RSA public and private key pairs.
    Return N, e, d
    - N must be the product of two random prime numbers p and q
    - e and d must be multiplicative inverses mod (p-1)(q-1)
    """
    p = generate_large_prime(bits)
    q = generate_large_prime(bits)
    w = (p-1)*(q-1)
    e = 1
    d = 1
    for t in primes:
        _, _, ze = ext_euclid(w, t)
        if ze == 1:
            e = ze
            break
    _, yd, _ = ext_euclid(w, e)
    d = yd
    return p*q, e, d
