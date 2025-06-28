'''
BOJ16313 - Janitor Troubles (https://www.acmicpc.net/problem/16313)

There are four lines.
Find the quadrilateral consisting of the four lines with the maximum area.
'''

# TIME COMPLEXITY : O(1)

import sys
from fractions import Fraction
from math import sqrt


# 1. TO GET THE INPUT

a, b, c, d = map(int, sys.stdin.readline().split())


# 2. TO SOLVE THE PROBLEM
# Search Bretschneider's Formula.

s = Fraction(a + b + c + d, 2)
print(sqrt((s - a)*(s - b)*(s - c)*(s - d)))