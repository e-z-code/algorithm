'''
BOJ34053 - Domino Game (https://www.acmicpc.net/problem/34053)

There is an N X M grid, non-integer in each cell.
You can repeat following moves.

(1) Choose two adjacent cells. At least one of them should be positive.
(2) Subtract 1 from chosen cells. If the number is 0, leave it without subtraction.

The game ends when all number becomes 0.
Determine the number of maximum repeat of moves you can make.
'''

# TIME COMPLEXITY : O(NM)

import sys


# 1. TO GET THE INPUT

row_count, col_count = map(int, sys.stdin.readline().split())

grid = []
for row_num in range(row_count):
    row = list(map(int, sys.stdin.readline().split()))
    grid.append(row)


# 2. TO SOLVE THE PROBLEM
# You can always start from the minimum value.

sum_val = 0
min_val = float('inf')

for row in range(row_count):
    for col in range(col_count):
        sum_val += grid[row][col]
        min_val = min(min_val, grid[row][col])

print(sum_val - min_val)