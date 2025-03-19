'''
BOJ30923 - 3D Printer (https://www.acmicpc.net/problem/30923)

Calculate the area of the outer area of the 3D histogram.
'''

# TIME COMPLEXITY : O(N)

import sys


# 1. TO GET THE INPUT

stick_count = int(sys.stdin.readline())
sticks = list(map(int, sys.stdin.readline().split()))


# 2. TO SOLVE THE PROBLEM

area = 0

area += sum(sticks) * 2
area += len(sticks) * 2
area += sticks[0] + sticks[-1]

for idx in range(1, stick_count):
    area += abs(sticks[idx] - sticks[idx - 1])

print(area)