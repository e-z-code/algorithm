'''
BOJ3996 - Great Fraud (https://www.acmicpc.net/problem/3996)

The number X is great if X (base K) = X (base -K).
Given N and K, determine the number of great numbers between 0 and N.
'''

# TIME COMPLEXITY : O(1)

import sys


# 1. TO GET THE INPUT

num, base = map(int, sys.stdin.readline().split())


# 2. TO SOLVE THE PROBLEM
# All coefficients of odd exponent must be 0.

arr = [0 for exp in range(41)]

# Find the maximum possible value

for exp in range(40, -1, -1):
    if pow(base * base, exp) <= num:
        digit = min(base - 1, num // pow(base * base, exp))
        arr[exp] = digit
        num -= digit * pow(base * base, exp)

# Count

ans = 1
for exp in range(41):
    digit = arr[exp]
    ans += digit * pow(base, exp)
print(ans)