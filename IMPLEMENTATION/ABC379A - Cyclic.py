'''
ABC379A - Cyclic (https://atcoder.jp/contests/abc379/tasks/abc379_a)

There is a three-digit integer N = ABC.
Print BCA and CAB.
'''

# TIME COMPLEXITY: O(1)

import sys


# 1. TO GET THE INPUT AND SOLVE THE PROBLEM

num = sys.stdin.readline().strip()

A, B, C = num[0], num[1], num[2]
print(B + C + A, C + A + B)