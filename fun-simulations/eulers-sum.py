
from random import random

"""
Get eulers number, using a monte-carlo-like
method. Wrap your head around this.
"""
def sum_to():
    total, iters = 0, 0
    while total < 1:
        total += random()
        iters += 1
    return iters

def history(iters=1000):
    results = [sum_to() for _ in range(iters)]
    return sum(results)/len(results)

print("eulers number is approximately...", history(10000000))
