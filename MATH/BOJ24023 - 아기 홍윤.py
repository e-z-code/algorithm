'''
BOJ24023 - Baby Hong (https://www.acmicpc.net/problem/24023)

Find a sub-array X of an array A of length N such that the result of bitwise OR of all elements of X equals K.
'''

# TIME COMPLEXITY : O(N)

import sys


# 1. TO GET THE INPUT

length, goal = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))


# 2. TO SOLVE THE PROBLEM

now = 0

start = None
end = None

for idx in range(length):
    
    if arr[idx] | goal == goal:
        if start == None:
            start = idx
            end = idx
        else:
            end = idx
        now |= arr[idx]
        if now == goal:
            break
    else:
        now = 0
        start = None
        end = None

if now == goal:
    print(start + 1, end + 1)
else:
    print(-1)