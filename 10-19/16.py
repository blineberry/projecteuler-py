# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
# What is the sum of the digits of the number 2^1000?

def sum_digits(digits):
    sum = 0

    for digit in str(digits):
        sum += int(digit)

    return sum

print(sum_digits(2**1000))