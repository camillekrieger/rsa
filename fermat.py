import argparse
import random


def prime_test(N: int, k: int) -> tuple[str, str]:
    return fermat(N, k), miller_rabin(N, k)

def mod_exp(x: int, y: int, N: int) -> int:
    if y == 0:
        return 1
    z = mod_exp(x, y//2, N)
    if y % 2 == 0:
        return (z**2) % N
    else:
        return (x * (z**2)) % N

def fprobability(k: int) -> float:
    return (1/2)**k

def mprobability(k: int) -> float:
    return (3/4)**k

def PrimeTest1(N):
    a = random.randint(1, N-1)
    if pow(a, N-1, N) == 1:
        return True
    else:
        return False

def fermat(N: int, k: int) -> str:
    for _ in range(k):
        if not PrimeTest1(N):
            return 'composite'
    return 'prime'

def millerPrime(N, overall, a):
    if pow(a, N, overall) == (overall - 1):
        return True
    if pow(a, N, overall) == 1:
        if (N) % 2 == 0:
            return millerPrime(((N)//2), overall, a)
        else:
            return True
    return False

def miller_rabin(N: int, k: int) -> str:
    for _ in range(k):
        a = random.randint(1, N-1)
        if not millerPrime(N-1, N, a):
            return 'composite'
    return 'prime'

def main(number: int, k: int):
    fermat_call, miller_rabin_call = prime_test(number, k)
    fermat_prob = fprobability(k)
    mr_prob = mprobability(k)

    print(f'Is {number} prime?')
    print(f'Fermat: {fermat_call} (prob={fermat_prob})')
    print(f'Miller-Rabin: {miller_rabin_call} (prob={mr_prob})')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('number', type=int)
    parser.add_argument('k', type=int)
    args = parser.parse_args()
    main(args.number, args.k)
