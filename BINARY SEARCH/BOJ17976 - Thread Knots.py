'''
BOJ17976 - Thread Knots (https://www.acmicpc.net/problem/17976)

There are N threads on the x-axis.
You want to make a knot in each thread.
Determine the maximum distance between the closest two neighboring knots.
'''

# TIME COMPLEXITY : O(N log X)

import sys


# 1. TO GET THE INPUT

thread_count = int(sys.stdin.readline())

threads = []
for thread in range(thread_count):
    start, length = map(int, sys.stdin.readline().split())
    threads.append((start, start + length))
threads.sort()


# 2. TO SOLVE THE PROBLEM

left = 0
right = pow(10, 10)

while left + 1 < right:
    
    mid = (left + right) // 2
    
    possible = True
    
    now = threads[0][0]
    for idx in range(1, thread_count):
        start, end = threads[idx]
        if now + mid <= end:
            now = max(now + mid, start)
        else:
            possible = False
            break
    
    if possible:
        left = mid
    else:
        right = mid

print(left)