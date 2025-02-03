'''
BOJ3359 - Swish Swish (https://www.acmicpc.net/problem/3359)

There are N rectangles.
You want to place them tightly on the axis in the given order.
Compute the maximum length of the upper envelope line.
'''

import sys


# 1. TO GET THE INPUT

square_count = int(sys.stdin.readline())

squares = []
for square in range(square_count):
    width, height = map(int, sys.stdin.readline().split())
    squares.append((width, height))


# 2. TO SOLVE THE PROBLEM
# dp[i][j] = Maximum length when placing i-th square in direction j 

dp = [[0, 0] for square in range(square_count)]

for idx in range(square_count):
    
    if idx == 0:
        dp[idx][0] = squares[idx][0]
        dp[idx][1] = squares[idx][1]
    else:
        dp[idx][0] = max(dp[idx-1][0] + squares[idx][0] + abs(squares[idx-1][1] - squares[idx][1]), dp[idx-1][1] + squares[idx][0] + abs(squares[idx-1][0] - squares[idx][1]))
        dp[idx][1] = max(dp[idx-1][0] + squares[idx][1] + abs(squares[idx-1][1] - squares[idx][0]), dp[idx-1][1] + squares[idx][1] + abs(squares[idx-1][0] - squares[idx][0]))

print(max(dp[-1]))