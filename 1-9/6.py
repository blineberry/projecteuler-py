# The sum of the squares of the first ten natural numbers is,
# 
#         1^2 + 2^2 + ... + 10^2 = 385
# 
# The square of the sum of the first ten natural numbers is,
# 
#         (1 + 2 + ... + 10)^2 == 55^2 = 3025
# 
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 
#         3025 - 385 = 2640
# 
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def sum_of_squares(start,stop):
    sum = 0

    for x in range(start, stop+1):
        sum = sum + x ** 2

    return sum

def square_of_sums(start,stop):
    return sum(range(start, stop+1)) ** 2

print(square_of_sums(1,100) - sum_of_squares(1,100))