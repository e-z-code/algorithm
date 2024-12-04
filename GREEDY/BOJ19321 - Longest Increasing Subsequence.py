'''
BOJ19321 - Longest Increasing Subsequence (https://www.acmicpc.net/problem/19321)

There is an array F.
Find a permutation P of integers from 1 to N such that F[i] is the length of LIS ending with P[i].
'''

# TIME COMPLEXITY : O(N log N)

import sys


# 1. TO GET THE INPUT

length = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))


# 2. TO SOLVE THE PROBLEM
# Fill from indices with low LIS length.
# If two or more indices have the same LIS length, fill from the largest index to the smallest.

ans = [0 for idx in range(length)]

info = []
for idx in range(length):
    info.append((arr[idx], idx))
info.sort(key = lambda x : (x[0], -x[1]))

num = 1
for lis_length, idx in info:
    ans[idx] = num
    num += 1

print(" ".join(map(str, ans)))