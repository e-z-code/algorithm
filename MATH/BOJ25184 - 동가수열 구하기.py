'''
BOJ25184 - Donga Sequence (https://www.acmicpc.net/problem/25184)

The following sequence is called the Donga sequence.

(1) A sequence X is a permutation of 1 ~ N.
(2) For all 1 <= i < N, N // 2 <= abs(A[i] - A[i-1])

Given N, construct a Donga sequence of length N.
'''

# TIME COMPLEXITY : O(N)

import sys


# 1. TO GET THE INPUT AND SOLVE THE PROBLEM

length = int(sys.stdin.readline())

ans = []

left = 1 + length // 2
right = 1

while left <= length:
    
    if right == 1 + length // 2:
        ans.append(left)
    else:
        ans.append(left)
        ans.append(right)
    
    left += 1
    right += 1

print(" ".join(map(str, ans)))