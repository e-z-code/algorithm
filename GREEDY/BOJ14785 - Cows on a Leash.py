'''
BOJ14785 - Cows on a Leash (https://www.acmicpc.net/problem/14785)

There are N lines.
You can select a point and delete all lines that include the point.
Determine the minimum number of operations necessary to delete all lines.
'''

# TIME COMPLEXITY : O(N log N)

import sys
from collections import deque
inf = float('inf')


# 1. TO GET THE INPUT

cow_count = int(sys.stdin.readline())

cows = []
for cow in range(cow_count):
    left, length = map(int, sys.stdin.readline().split())
    cows.append((left + length, left))

cows.sort()


# 2. TO SOLVE THE PROBLEM
# The problem is equivalent to "interval scheduling" problem.

ans = 0
rightmost = 0

for right, left in cows:
    if rightmost <= left:
        ans += 1
        rightmost = right

print(ans)