'''
BOJ17075 - Restoration (https://www.acmicpc.net/problem/17075)

There is an N X M binary matrix.
Fill the matrix such that the sum of all sums of sub-rectangles is a multiple of K.
'''

# TIME COMPLEXITY : O(NMK) 

import sys


# 1. TO GET THE INPUT

row_count, col_count, mod = map(int, sys.stdin.readline().split())

grid = []
for row in range(row_count):
    grid.append(list(map(int, sys.stdin.readline().split())))


# 2. TO GET POSSIBLE ITEMS

now_val = 0
items = [(-1, -1, -1)]

for row in range(row_count):
    for col in range(col_count):
        val = (row + 1) * (row_count - row) * (col + 1) * (col_count - col)
        if grid[row][col] == 1:
            now_val += val
        elif grid[row][col] == -1:
            items.append((row, col, val))


# 3. DP
# DP[i][j] = If it is possible to make j mod K using the first i items.

dp = [[(None, None, None) for remainder in range(mod)] for item in range(len(items))]

dp[0][now_val % mod] = (-1, -1, 0)

for idx in range(1, len(items)):
    row, col, val = items[idx]
    for remainder in range(mod):
        if dp[idx-1][remainder] != (None, None, None):
            dp[idx][remainder] = (-1, -1, remainder)
        if dp[idx-1][(remainder - val) % mod] != (None, None, None):
            dp[idx][remainder] = (row, col, (remainder - val) % mod)


# 4. TO SOLVE THE PROBLEM

if dp[-1][0] == (None, None, None):
    
    print(-1)
    
else:
    
    print(1)
    
    now_mod = 0

    for idx in range(len(items) - 1, 0, -1):
        row, col, last_mod = dp[idx][now_mod]
        if not (row == -1 and col == -1):
            grid[row][col] = 1
        now_mod = last_mod
    
    for row in range(row_count):
        for col in range(col_count):
            if grid[row][col] == -1:
                grid[row][col] = 0
        print(" ".join(map(str, grid[row])))