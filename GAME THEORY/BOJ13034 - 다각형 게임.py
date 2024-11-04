'''
BOJ13034 - Polygon Game (https://www.acmicpc.net/problem/13034)

There are N vertices of a convex polygon.
At each turn, a player can choose two vertices and draw a segment.
However, the segment must not meet with any other segments.
The player who cannot draw a segment loses.
Assuming each player makes the optimal move, determine who will win the game.
'''

# CLASS 7
# TIME COMPLEXITY : O(N^2)

import sys


# 1. TO CALCULATE GRUNDY NUMBERS

grundy = [0 for num in range(1001)]

# Let N, the number of points, represent a game state.
# The set of possible next game states of N are {(N-2, 0), (N-3, 1), ..., (0, N-2)}

for num in range(2, 1001):
    
    next_state_grundy = set()
    for i in range(num // 2):
        next_state_grundy.add(grundy[i] ^ grundy[num-2-i]) # Grundy number of multiple games can be calculated using XOR operation.
    
    result = 0
    while True:
        if result in next_state_grundy:
            result += 1
        else:
            grundy[num] = result
            break


# 2. TO SOLVE THE PROBLEM
# The first player wins if the Grundy number of the start state is not 0.
# Otherwise, the first player loses.

point_count = int(sys.stdin.readline())

if grundy[point_count] != 0: 
    print(1)
else:
    print(2)