'''
ABC418A - I'm a teapot (https://atcoder.jp/contests/abc418/tasks/abc418_a)

Determine if a given string of length N ends with 'tea'.
'''

# TIME COMPLEXITY: O(N)

import sys


# 1. TO GET THE INPUT

length = int(sys.stdin.readline())
liquid = sys.stdin.readline().strip()


# 2. TO SOLVE THE PROBLEM

if len(liquid) >= 3 and liquid[-3:] == "tea":
    print("Yes")
else:
    print("No")