
from random import random

"""
Get eulers number, using a monte-carlo-like
method. Wrap your head around this.

Eulers is the conception that something small
will extrapolate to infinite, but it does quite
the opposite. It spreads its wings, then falls
on 2.718 and so-forth.

Compare how E relates to everything.
36% is roughly 1/e.

The closer to E, the larger maximization
is possible given a division.
"""
def sum_to():
    total, iters = 0, 0
    while total < 1:
        total += random()
        iters += 1
    return iters

# a iter-then-calculate approach.
def history(iters=1000):
    results = [sum_to() for _ in range(iters)]
    return sum(results)/len(results)

# a calculate-as-iter approach.
def sequential_history(iters=3):
    value = 0
    for i in range(iters):
        value += sum_to()
    average = value/(i+1)
    return average

# sequential_history()
print("eulers number is approximately...", sequential_history(1000000))
