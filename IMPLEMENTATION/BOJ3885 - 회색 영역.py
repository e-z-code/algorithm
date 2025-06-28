'''
BOJ3885 - Grey Area (https://www.acmicpc.net/problem/3885)

The height of the histogram is fixed to 1.
That is, the height of the highest bar is always the same, and others are automatically adjusted proportionately.
The widths of the bars are also fixed.
The colors of the leftmost and the rightmost bars are black and white.
The darkness of other bars monotonically decreases at the same rate from left to right.

Given values for the histogram, determine the quantity of inks needed to color the histogram.
'''

# TIME COMPLEXITY : O(max(N, 100/W))

import sys
from fractions import Fraction


# 1. TO GET THE INPUT

while True:
    
    value_count, interval_length = map(int, sys.stdin.readline().split())
    if value_count == 0 and interval_length == 0:
        break

    histogram = [0 for interval in range(102)]

    for idx in range(value_count):
        value = int(sys.stdin.readline())
        histogram[value // interval_length] += 1

    while histogram[-1] == 0:
        histogram.pop()


    # 2. TO SOLVE THE PROBLEM

    max_height = 0
    for height in histogram:
        max_height = max(height, max_height)

    ans = Fraction(1, 100)
    for idx in range(len(histogram)):
        ans += Fraction(histogram[idx], max_height) * Fraction(len(histogram) - 1 - idx, len(histogram) - 1)
    print(float(ans))