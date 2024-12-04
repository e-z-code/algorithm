'''
BOJ2104 - Choose a substring (https://www.acmicpc.net/problem/2104)

There is an array A of length N.
The point of (i, j) equals (A[i] + ... + A[j]) X min(A[i], ..., A[j]).
Determine the maximum point possible.
'''

# TIME COMPLEXITY : O(N log N)

import sys
from bisect import bisect_left, insort_left


# 1. TO GET THE INPUT

length = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))


# 2. PREFIX SUM

prefix_sum = [0] + arr[:]
for idx in range(1, length + 1):
    prefix_sum[idx] += prefix_sum[idx-1]


# 3. TO SOLVE THE PROBLEM

# To store indices of each element

info = []
for idx in range(length):
    info.append((arr[idx], idx + 1))
info.sort()

# For each element X, using binary search, it is possible to find the maximum length substring of which minimum value is X.

ans = 0

bound = [0, length + 1]
for element, loc in info:

    idx = bisect_left(bound, loc)
    left_end, right_end = bound[idx-1] + 1, bound[idx] - 1
    ans = max(ans, element * (prefix_sum[right_end] - prefix_sum[left_end - 1]))
    insort_left(bound, loc)

print(ans)
