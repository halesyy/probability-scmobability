
from random import random

def roll_return():
    top, bottom = 1, 6
    win = random() > top/(bottom*1.001)
    perc = 1+(top/bottom) if win else -1
    return win, perc

# bet 1%
# bet 2% if 1 in last 3 history
# bet 4% if 1 in last 3 history
# bet 8% if 1 in last 3 history
def history(iters=100):
    starting_balance = 1000
    balance = starting_balance
    balance_history = [balance]
    history = [False, False, False]
    # calc the bet size at each iter
    def calc_bet_size(balance, latest_history):
        start_perc = 1
        # 1, 2, 4, 8
        for _ in range(sum(latest_history)):
            start_perc *= 2
        percentage = start_perc / 100
        return balance * percentage
    # simulation iterations
    for i in range(iters):
        bet_size = calc_bet_size(balance, history[-3:])
        win, return_on_trade = roll_return()
        # print(return_on_trade)
        history.append(win) # add for future calc work
        # calc new balance, add to balance history
        balance += bet_size*return_on_trade
        # print(balance, bet_size*return_on_trade)
        balance_history.append(balance)
    # print(balance_history[-1])
    return (balance_history[-1]/starting_balance)-1

# history()
histories = [history() for _ in range(10000)]
print("> average:", sum(histories)/len(histories))
