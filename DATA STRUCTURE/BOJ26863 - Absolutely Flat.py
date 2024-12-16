'''
BOJ26863 - Absolutely Flat (https://www.acmicpc.net/problem/26863)

There is a table of four legs of length P, Q, R, and S.
You can attach a pad of length B to one of the legs.
Determine if it is possible to make the table flat.
'''

# TIME COMPLEXITY : O(1)

import sys


# 1. TO GET THE INPUT

legs = []
for leg in range(4):
    legs.append(int(sys.stdin.readline()))
legs.sort()

pad = int(sys.stdin.readline())


# 2. TO SOLVE THE PROBLEM

if len(set(legs)) == 1:
    print(1)
else:
    legs[0] += pad
    if len(set(legs)) == 1:
        print(1)
    else:
        print(0)