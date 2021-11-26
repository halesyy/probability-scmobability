
from random import randint, choice

def sample():
    # given working data
    start = [0, 0] # 2d matrix
    moves = 0
    history = []
    # iterate-till-death
    while True:
        history.append([start[0],start[1]]) # copy
        start[randint(0, 1)] += choice([-1, 1])
        moves += 1
        if start[0] == 0 and start[1] == 0:
            break
        if moves > 10000: # breakout
            return (False, False)
    # return given a while break
    return (moves, history)

# moves, history = sample()
res = [sample()[0] for _ in range(100000)]
res = [r for r in res if r != False]

# print results
print("> the avg moves to get home with a 10,000 iter breakpoint is: {:.2f}".format(
    sum(res)/len(res)
))

# time to plot, plot if needed
# import matplotlib.pyplot as plt
# moves, history = sample()
# plt.scatter([x[0] for x in history], [y[1] for y in history])
# plt.show()
