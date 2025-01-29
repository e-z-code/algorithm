'''
BOJ2655 - The Highest Tower (https://www.acmicpc.net/problem/2655)

There are N bricks.
You can put brick X on top of brick Y if and only if the following holds:

(1) The floor area of Y is larger than the floor area of X.
(2) Y is heavier than X.

Determine the height of the highest tower and its composites.
'''

# TIME COMPLEXITY : O(N^2)

import sys


# 1. TO GET THE INPUT

brick_count = int(sys.stdin.readline())

bricks = []
for brick in range(brick_count):
    floor_area, height, weight = map(int, sys.stdin.readline().split())
    bricks.append((floor_area, height, weight, brick+1))

bricks.sort(reverse=True)


# 2. DP

dp = [bricks[idx][1] for idx in range(brick_count)]
prev = [-1 for idx in range(brick_count)]

for i in range(1, brick_count):
    for j in range(i):
        if bricks[j][2] > bricks[i][2] and dp[j] + bricks[i][1] > dp[i]:
            dp[i] = dp[j] + bricks[i][1]
            prev[i] = j


# 3. TRACE

max_idx = None
max_val = 0

for idx in range(brick_count):
    if dp[idx] > max_val:
        max_idx = idx
        max_val = dp[idx]

ans = []

while max_idx != -1:
    ans.append(bricks[max_idx][3])
    max_idx = prev[max_idx]

print(len(ans))
for brick_num in ans:
    print(brick_num)