# If we list all the natural numbers below 10 that are multiples of 3 or 5, 
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# 
# Find the sum of all the multiples of 3 or 5 below 1000.

def natural_numbers_sum(limit):
    sum = 0
    for x in range(limit):
        if x % 3 != 0 and x % 5 != 0:
            continue

        sum += x
    
    print(sum)

natural_numbers_sum(1000)