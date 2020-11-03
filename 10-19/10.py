# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# 
# Find the sum of all the primes below two million.

import math

def is_prime(i):
    if i == 2:
        return True

    if i % 2 == 0:
        return False

    for x in range(3, int(math.sqrt(i)) + 1):
        if i % x == 0:
            return False

    return True

def get_primes_below(ceiling):
    primes = [2]

    for i in range(3,ceiling,2):
        if is_prime(i):
            primes.append(i)

    return primes

print(sum(get_primes_below(2000000)))