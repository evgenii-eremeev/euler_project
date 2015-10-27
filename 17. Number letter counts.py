"""
https://projecteuler.net/problem=17
If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two)
contains 23 letters and 115 (one hundred and fifteen) contains 20 letters.
The use of "and" when writing out numbers is in compliance with British usage.
"""

NUMBERS = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
    1000: 'onethousand',
}

def count_letters(limit=1000):
    total_len = 0
    for num in range(1, limit + 1):
        if num in NUMBERS.keys():
            total_len += len(NUMBERS[num])
        elif num < 100:
            total_len += len(NUMBERS[num // 10 * 10] + NUMBERS[num % 10])
        else:
            total_len += len(NUMBERS[num // 100]) + len('hundred')
            test = NUMBERS[num // 100] + 'hundred'
            if num % 100 == 0:
                continue
            elif num % 100 in NUMBERS.keys():
                total_len += len('and') + len(NUMBERS[num % 100])
                test += 'and' + NUMBERS[num % 100]
            else:
                total_len += len('and')
                total_len += len(NUMBERS[num % 100 // 10 * 10])
                total_len += len(NUMBERS[num % 100 % 10])
                test += 'and' + NUMBERS[num % 100 // 10 * 10] + NUMBERS[num % 100 % 10]
    return total_len


# answer
print(count_letters(1000))
