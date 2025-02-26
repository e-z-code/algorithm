'''
BOJ10937 - Cutting Tofu (https://www.acmicpc.net/problem/10937)

There is an N X N tofu.
You can cut tofu and sell either 1 X 2 or 2 X 1 blocks.
Each tofu cell is of a certain quality, and the price of the block is determined according to the quality of the cells.
Determine the maximum revenue you can earn.
'''

# TIME COMPLEXITY : O(pow(2, N) X pow(N, 2))

import sys
inf = float('inf')


# 2. DP FUNCTION

def fill_table(now, case):
    
    row, col = now // size, now % size
    
    # Base Case
    if now == size * size:
        return 0
    
    # Memoization
    if dp[now][case] != -1:
        return dp[now][case]

    # Not choose
    best = fill_table(now+1, case >> 1)
    if case & 1 == 0:
        # Choose horizontal group
        if col != size - 1 and case & 2 == 0:
            best = max(best, fill_table(now + 2, case >> 2) + point.get(grid[row][col] + grid[row][col+1], 0))
        # Choose vertical group
        if row != size - 1:
            best = max(best, fill_table(now + 1, (case >> 1) | (1 << (size - 1))) + point.get(grid[row][col] + grid[row+1][col], 0))
    dp[now][case] = best
    
    return best


# 1. TO GET THE INPUT

size = int(sys.stdin.readline())
point = {"AA":100, "AB":70, "BA":70, "BB":50, "AC":40, "CA":40, "BC":30, "CB":30, "CC":20}

grid = []
for row in range(size):
    grid.append(list(sys.stdin.readline().strip()))


# 3. TO SOLVE THE PROBLEM
# dp[X][Y] = The maximum value when starting from X and the state of next S cells are Y. [S = size]

dp = [[-1 for case in range(1 << size)] for start in range(size * size)]
print(fill_table(0, 0))