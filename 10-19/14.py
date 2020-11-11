# The following iterative sequence is defined for the set of positive integers:
#
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
#
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.

collatz_sequences = {}

def get_next_collatz_num(current_num):
    if current_num % 2 == 0:
        return int(current_num / 2)

    return current_num * 3 + 1

def get_collatz_sequence(starting_num):
    sequence = [starting_num]

    while sequence[-1] != 1:
        last_num = sequence[-1]
        if last_num in collatz_sequences:
            sequence.pop()
            sequence.extend(collatz_sequences[last_num])
            break

        sequence.append(get_next_collatz_num(last_num))

    collatz_sequences[starting_num] = sequence
    return sequence

def get_collatz_sequence_count(starting_num):
    return len(get_collatz_sequence(starting_num))

def get_collatz_starting_num_with_longest_chain(starting_num_limit):
    longest_chain_count = 1
    longest_chain_starting_num = 1

    for starting_num in range(1, starting_num_limit, 1):
        count = get_collatz_sequence_count(starting_num)

        if count > longest_chain_count:
            longest_chain_count = count
            longest_chain_starting_num = starting_num

    return longest_chain_starting_num

print(get_collatz_starting_num_with_longest_chain(999999))
