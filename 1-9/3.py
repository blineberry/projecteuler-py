# The prime factors of 13195 are 5, 7, 13 and 29.
# 
# What is the largest prime factor of the number 600851475143 ?

def is_prime(i):
    if i == 2:
        return True

    if i % 2 == 0:
        return False

    for x in range(3, i + 1 // 2):
        if i % x == 0:
            return False

    return True

def get_factors_desc(i):
    f1s = []
    f2s = []

    for x in range(1, i, 1):
        if i % x != 0:
            continue

        f2 = i // x

        if f2 < x:
            break
        
        f1s.insert(0, x)
        f2s.append(f2)

    f2s.extend(f1s)

    return f2s

def get_first_prime(l):
    for x in l:
        if is_prime(x):
            return x

print(get_first_prime(get_factors_desc(600851475143)))