'''
BOJ30905 - Higher Arithmetic (https://www.acmicpc.net/problem/30905)

Given N integers, construct an arithmetic expression with the maximal value.
'''

# TIME COMPLEXITY : O(N log N)

import sys


# 1. TO GET THE INPUT

length = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort(reverse=True)


# 2. TO SOLVE THE PROBLEM

one_count = 0
two_count = 0

# Leave all numbers but one and two.

while len(arr) != 0 and arr[-1] <= 2:
    if arr[-1] == 1:
        one_count += 1
    else:
        two_count += 1
    arr.pop()
arr = list(map(str, arr))

# Make as many threes as possible.

while min(one_count, two_count) != 0:
    arr.append("(1+2)")
    one_count -= 1
    two_count -= 1

while two_count != 0:
    arr.append("2")
    two_count -= 1

while one_count != 0:
    if one_count == 1: 
        if len(arr) == 0:
            arr.append("1")
        else:
            arr.append("(" + arr.pop() + "+1)")
        one_count -= 1
    elif one_count == 2:
        arr.append("(1+1)")
        one_count -= 2
    else:
        arr.append("(1+1+1)")
        one_count -= 3

print("*".join(arr))