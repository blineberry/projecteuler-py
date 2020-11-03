# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a2 + b2 = c2
# 
# For example, 32 + 42 = 9 + 16 = 25 = 52.
# 
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

import math

def get_pythagorean_c(a,b):
    return math.sqrt(a**2 + b**2)

def is_pythagorean_triplet(a,b,c=None):
    if c is None:
        c = get_pythagorean_c(a,b)

    if not c.is_integer():
        return False

    return a**2 + b**2 == c**2

def get_pythagorean_triplets(range_stop):
    triplets = []

    for a in range(0,range_stop):
        for b in range(a + 1,range_stop):
            c = get_pythagorean_c(a,b)

            if c <= b:
                continue

            if is_pythagorean_triplet(a,b,c):
                triplets.append((a,b,c))

    return triplets

def get_pythagorean_triplet_where_sum_equals(s):
    triplets = get_pythagorean_triplets(s // 2)

    for triplet in triplets:
        if sum(triplet) == s:
            return triplet

def get_product(t):
    return math.prod(t)

print(get_product(get_pythagorean_triplet_where_sum_equals(1000)))