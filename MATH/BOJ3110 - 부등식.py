'''
BOJ3110 - Inequality (https://www.acmicpc.net/problem/3110)

(a2 / a1) < (b2 / b1) < (c2 / c1) < (d2 / d1) < (e2 / e1)

Determine the number of triples (b2, c2, d2) that satisfies the inequality above.
The values of all other variables are given.
'''

# TIME COMPLEXITY : O(C X E1)

import sys


# 1. TO GET THE INPUT

b1, c1, d1 = map(int, sys.stdin.readline().split())
a2, a1 = map(int, sys.stdin.readline().split())
e2, e1 = map(int, sys.stdin.readline().split())


# 2. TO SOLVE THE PROBLEM

ans = 0

for c2 in range(1000001):
    
    b2_lowest = b1 * a2 // a1 + 1
    b2_highest = b1 * c2 // c1
    if (b1 * c2) % c1 == 0:
        b2_highest -= 1
    
    d2_lowest = d1 * c2 // c1 + 1
    d2_highest = d1 * e2 // e1
    if (d1 * e2) % e1 == 0:
        d2_highest -= 1
    
    if b2_lowest <= b2_highest and d2_lowest <= d2_highest:
        ans += (b2_highest - b2_lowest + 1) * (d2_highest - d2_lowest + 1)

print(ans)