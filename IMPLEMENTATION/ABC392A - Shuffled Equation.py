'''
ABC392A - Shuffled Equation (https://atcoder.jp/contests/abc392/tasks/abc392_a)

You are given a sequence of integers A = (x, y, z).
Let B = (a, b, c) be any permutation of A.
Determine if there is such a case that a X b = c.
'''

# TIME COMPLEXITY: O(1)

import sys


# 1. TO GET THE INPUT AND SOLVE THE PROBLEM

x, y, z = map(int, sys.stdin.readline().split())

ans = "No"

if x * y == z:
    ans = "Yes"
if x * z == y:
    ans = "Yes"
if y * x == z:
    ans = "Yes"
if y * z == x:
    ans = "Yes"
if z * x == y:
    ans = "Yes"
if z * y == x:
    ans = "Yes"

print(ans)