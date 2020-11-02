# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# 
# Find the largest palindrome made from the product of two 3-digit numbers.

def get_products_desc(range1start, range1stop, range2start,range2stop):
    products = []

    for x in range(range1start, range1stop):
        for y in range(range2start, range2stop):
            products.append(x * y)

    products.sort(reverse=True)

    return products

def is_palindromic(i):
    return str(i) == str(i)[::-1]

def get_first_palindromic_number(l):
    for x in l:
        if is_palindromic(x):
            return x

print(get_first_palindromic_number(get_products_desc(100,1000, 100,1000)))