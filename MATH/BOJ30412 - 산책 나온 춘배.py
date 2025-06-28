'''
BOJ30412 - Choon-Bae on Walk  (https://www.acmicpc.net/problem/30412)

There is an array A of length N.
In one operation, you can choose an element and increase it by 1.
Your goal is to make an index i such that abs(A[i] - A[i-1]) >= X and abs(A[i] - A[i+1]) >= X.
Determine the minimum operations needed.
'''

# TIME COMPLEXITY : O(N)

import sys


# 1. TO GET THE INPUT

length, goal_diff = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))


# 2. TO SOLVE THE PROBLEM

ans = float('inf')

for idx in range(length):
    
    if idx == 0:
        now_count = max(0, goal_diff - abs(arr[idx+1] - arr[idx]))
    elif idx == length - 1:
        now_count = max(0, goal_diff - abs(arr[idx] - arr[idx-1]))
    else:
        left, mid, right = arr[idx-1], arr[idx], arr[idx+1]
        if left <= mid:
            if right <= mid:
                now_count = max(0, max(left + goal_diff, right + goal_diff) - mid)
            else:
                now_count = max(0, left + goal_diff - mid)
                mid = max(mid, left + goal_diff)
                now_count += max(0, mid + goal_diff - right)
        else:
            if right <= mid:
                now_count = max(0, right + goal_diff - mid)
                mid = max(mid, right + goal_diff)
                now_count += max(0, mid + goal_diff - left)
            else:
                caseA = max(0, mid + goal_diff - left) + max(0, mid + goal_diff - right)
                caseB = max(0, max(left + goal_diff, right + goal_diff) - mid)
                now_count = min(caseA, caseB)
        
    ans = min(ans, now_count)

print(ans)