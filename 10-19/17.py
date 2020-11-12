# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
#
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

ones = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["zero", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

def write_out_number(num):
    if num == 1000:
        return "one thousand"

    if num < 10:
        return ones[num]
    
    if num < 20:
        return teens[num - 10]

    if num < 100:
        tens_index = num // 10

        if num % 10 == 0:
            return tens[tens_index]

        return tens[tens_index] + " " +  write_out_number(num - tens_index * 10)

    if num < 1000:
        hundreds_index = num // 100

        if num % 100 == 0:
            return ones[hundreds_index] + " hundred"

        return ones[hundreds_index] + " hundred and " + write_out_number(num - hundreds_index * 100)

def get_written_out_numbers_for_range(r):
    return list(map(write_out_number, r))

def count_letters(s):
    return len(s.replace(" ", ""))

def count_letters_in_list(l):
    return sum(map(count_letters, l))

print(count_letters_in_list(get_written_out_numbers_for_range(range(1,1001))))