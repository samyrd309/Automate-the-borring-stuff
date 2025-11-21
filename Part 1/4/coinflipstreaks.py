import random
numberOfStreaks = 0
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    coinflip = []
    for i in range(100):
        if random.randint(0,1) == 0:
            coinflip.append('T') # add living cell
        else:
            coinflip.append('H') # add dead cell
    # Code that checks if there is a streak of 6 heads or tails in a row.
    currentStreak = 0
    for i in range(1, len(coinflip)):
        if coinflip[i] == coinflip[i-1]:
            currentStreak += 1
        else: 
            currentStreak = 1

        if currentStreak >= 6:
            numberOfStreaks += 1
            break

print('Chance of streak: %s%%' % (numberOfStreaks / 100))