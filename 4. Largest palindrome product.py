"""
https://projecteuler.net/problem=4
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""


def is_pal(inp):
    """
    Is palindrom?
    Returns True if num or str is palindrom.
    """
    inp = str(inp)
    if len(inp) <= 1:
        return True
    return inp[0] == inp[-1] and is_pal(inp[1:-1])


def largest_pal_product(num1, num2):
    """
    Finds largest palindrom from products of numbers from num1 to num2
    :param num1: int
    :param num2: int
    :return: int
    """
    largest = 0
    for i in range(num1 + 1):
        for j in range(num2 + 1):
            product = i * j
            if is_pal(product) and product > largest:
                largest = product
    return largest

# answer
print(largest_pal_product(999, 999))
