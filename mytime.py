"""Simple timing module written by myself"""

import time

def mytime(func, *args, **kwargs):
    """
    Measuring execution time of given function.
    Input: function, parameters of the function.
    Output: Time taken to execute the function.
    """
    start = time.clock()
    func(*args, **kwargs)
    return time.clock() - start
