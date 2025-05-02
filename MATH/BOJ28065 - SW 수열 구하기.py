'''
BOJ28065 - SW Sequence (https://www.acmicpc.net/problem/28065)

The following sequence is called the SW sequence.

(1) A sequence A is a permutation of 1 ~ N.
(2) For all 1 < i < N, abs(A[i] - A[i-1]) > abs(A[i+1] - A[i])

Given N, construct an SW sequence of length N.
'''

# TIME COMPLEXITY : O(N)

import sys


# 1. TO GET THE INPUT AND SOLVE THE PROBLEM

length = int(sys.stdin.readline())

ans = []

left = length
right = 1
while left >= right:
    if left != right:
        ans.append(left)
        ans.append(right)
    else:
        ans.append(left)
    left -= 1
    right += 1

print(" ".join(map(str, ans)))