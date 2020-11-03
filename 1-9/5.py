# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# 
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def smallest_num_divisible_by_range(start, stop):
    testnum = stop

    while True:
        is_divisible = True

        for x in range(stop, start, -1):
            if testnum % x != 0:
                is_divisible = False
                break

        if is_divisible:
            break

        testnum = testnum + stop

    return testnum

print(smallest_num_divisible_by_range(1,20))