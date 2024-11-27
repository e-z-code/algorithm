'''
BOJ18101 - Regular Sub-polygon (https://www.acmicpc.net/problem/18101)

Given a polygon of N vertices, determine the smallest number of vertices to form a regular polygon.
'''

# TIME COMPLEXITY : O(sqrt N)

import sys


# 1. TO GET THE INPUT

num = int(sys.stdin.readline())


# 2. TO SOLVE THE PROBLEM
# The problem is equivalent to get the minimum divisor more than or equal to 3.

ans = None

for divisor in range(3, int(num ** 0.5) + 1):
    if num % divisor == 0:
        ans = divisor
        break

if ans != None:
    print(ans)
else:
    if num % 2 == 0:
        if num == 4:
            print(num)
        else:
            print(num // 2)
    else:
        print(num)