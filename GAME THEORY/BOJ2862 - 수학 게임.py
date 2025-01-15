'''
BOJ2862 - Math Game (https://www.acmicpc.net/problem/2862)

There are N coins.
Two players alternatively take one or more coins.
You play first. At first move, you can take 1 <= X <= N coins.
If an opponent takes Y coins at the last move, the other player can take 1 <= X <= 2Y coins at the next move.
Determine the minimum number of coins you need to take at the first move to win the game.
'''

# TIME COMPLEXITY : O(log N)

import sys


# 1. TO GET THE FIBONACCI NUMBERS

fibonacci = [1, 2]

while True:
    new_num = fibonacci[-1] + fibonacci[-2]
    if new_num <= pow(10, 15):
        fibonacci.append(new_num)
    else:
        break


# 2. TO GET THE INPUT AND SOLVE THE PROBLEM
# The game is known as "Fibonacci NIM" game.
# The answer is the smallest term in Zeckendorf representation.

coin_count = int(sys.stdin.readline())

while True:
    if coin_count in fibonacci:
        print(coin_count)
        break
    else:
        for idx in range(len(fibonacci) - 1):
            if fibonacci[idx] < coin_count < fibonacci[idx+1]:
                coin_count -= fibonacci[idx]