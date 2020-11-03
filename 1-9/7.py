# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# 
# What is the 10 001st prime number?

def is_prime(i):
    if i == 2:
        return True

    if i % 2 == 0:
        return False

    for x in range(3, i + 1 // 2):
        if i % x == 0:
            return False

    return True

def get_n_prime(n):
    primes = [2, 3]

    while len(primes) < n:
        i = primes[-1] + 2

        while True:
            if is_prime(i):
                primes.append(i)
                break

            i += 2
    
    return primes[n-1]

print(get_n_prime(10001))