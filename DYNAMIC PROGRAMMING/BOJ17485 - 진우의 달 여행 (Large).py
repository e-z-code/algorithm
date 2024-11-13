'''
BOJ17485 - Moon Travel (https://www.acmicpc.net/problem/17485)

There is an N X M cost that connects the Earth and the Moon and denotes the cost to pass each area.
Your satellite cannot move consecutively in the same direction. 
Determine the minimum cost from the Earth to the Moon.
'''

# TIME COMPLEXITY : O(NM)

import sys
inf = float('inf')


# 1. TO GET THE INPUT

row_count, col_count = map(int, sys.stdin.readline().split())

cost = []
for row in range(row_count):
    row_input = list(map(int, sys.stdin.readline().split()))
    cost.append(row_input)


# 2. DYNAMIC PROGRAMMING
# dp[i][j][d] = The minimum cost to arrive (i, j) with the last direction of d.
# d : 0 (Below Left), 1 (Straight Below), 2 (Below Right)

dp = [[[inf for d in range(3)] for j in range(col_count)] for i in range(row_count)]

for i in range(row_count):
    for j in range(col_count):
        
        if i == 0:
            for d in range(3):
                dp[i][j][d] = cost[i][j] # You can start with any direction.
        else:
            if j != col_count - 1:
                dp[i][j][0] = min(dp[i-1][j+1][1], dp[i-1][j+1][2]) + cost[i][j]
            dp[i][j][1] = min(dp[i-1][j][0], dp[i-1][j][2]) + cost[i][j]
            if j != 0:
                dp[i][j][2] = min(dp[i-1][j-1][0], dp[i-1][j-1][1]) + cost[i][j]


# 3.  TO SOLVE THE PROBLEM

ans = inf
for j in range(col_count):
    for d in range(3):
        ans = min(ans, dp[-1][j][d])
print(ans)