'''
BOJ3164 - Pattern (https://www.acmicpc.net/problem/3164)

Given a rectangle and a pattern, determine the number of black squares the rectangle includes.
'''

# TIME COMPLEXITY : O(max(x2, y2))

import sys


# 1. TO GET THE INPUT

x1, y1, x2, y2 = map(int, sys.stdin.readline().split())


# 2. TO SOLVE THE PROBLEM

ans = 0

# Squares included in horizontal lines
for y in range(y1 + 1, y2 + 1):
    if y % 2 == 0:
        if x1 < y:
            ans += min(x2, y) - x1

# Squares included in vertical lines
for x in range(x1 + 1, x2 + 1):
    if x % 2 == 0:
        if y1 < x:
            ans += min(y2, x) - y1

# Squares included in both
for i in range(2, 1000001, 2):
    if x1 < i <= x2 and y1 < i <= y2:
        ans -= 1

print(ans)