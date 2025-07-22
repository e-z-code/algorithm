'''
BOJ15154 - Lights in the Morning (https://www.acmicpc.net/problem/15154)

There are N traffic lights.
The X-th light will first turn green at A[X] seconds.
Then, it will remain green for B[X] seconds, then change to red for C[X] seconds, and so on.
Determine if it is possible to complete your journey without getting stopped by traffic lights.
'''

# TIME COMPLEXITY : O(N)

import sys


# 1. TO GET THE INPUT AND SOLVE THE PROBLEM

light_count, length = map(int, sys.stdin.readline().split())

ans = "YES"
for light in range(light_count):
    loc, start_time, green_time, red_time = map(int, sys.stdin.readline().split())
    if loc < start_time:
        ans = "NO"
    else:
        if 0 <= (loc - start_time) % (green_time + red_time) <= green_time:
            continue
        else:
            ans = "NO"

print(ans)