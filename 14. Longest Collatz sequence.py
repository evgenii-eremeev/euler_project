"""
https://projecteuler.net/problem=14
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?
"""


def collatz(num):
    seq = [num]
    while num != 1:
        if num % 2 == 0:
            num //= 2
            seq.append(num)
        else:
            num = 3 * num + 1
            seq.append(num)
    return seq


def longest_collatz(limit):
    used = set()
    longest_len = 1
    longest_num = 1
    for i in range(limit, 1, -1):
        if i in used:
            continue
        elems = collatz(i)
        used.update(elems)
        length_i = len(elems)
        if length_i > longest_len:
            longest_len = length_i
            longest_num = i
    return longest_num


lim = 1000000
# answer
print(longest_collatz(lim))
