'''
BOJ23083 - Honeybee (https://www.acmicpc.net/problem/23083)

There is a hive consisting of N X M hexagon cells.
In the same row, columns of even index are located half cell below columns of odd index.
You can only move to adjacent cells on the right or below.
Determine the number of cases to reach (N, M) from (1, 1).
'''

# TIME COMPLEXITY : O(N log N) 

import sys
MOD = pow(10, 9) + 7


# 1. TO GET THE INPUT

row_count, col_count = map(int, sys.stdin.readline().split())

grid = [[1 for col in range(col_count)] for row in range(row_count)]

hole_count = int(sys.stdin.readline())
for hole in range(hole_count):
    row, col = map(int, sys.stdin.readline().split())
    grid[row-1][col-1] = 0


# 2. DP
# dp[i][j] = Number of valid paths to (i, j)

dp = [[0 for col in range(col_count)] for row in range(row_count)]

dp[0][0] = 1

for col in range(col_count):
    for row in range(row_count):
        
        if grid[row][col] == 0:
            continue
        else:
            
            if col % 2 == 0:
                if 0 <= row-1 < row_count and 0 <= col-1 < col_count:
                    dp[row][col] += dp[row-1][col-1]
            else:
                if 0 <= row+1 < row_count and 0 <= col-1 < col_count:
                    dp[row][col] += dp[row+1][col-1]
            
            if 0 <= row-1 < row_count and 0 <= col < col_count:
                dp[row][col] += dp[row-1][col]
            if 0 <= row < row_count and 0 <= col-1 < col_count:
                dp[row][col] += dp[row][col-1]
            
            dp[row][col] %= MOD

print(dp[-1][-1])