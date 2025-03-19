'''
BOJ2374 - Make It Identical (https://www.acmicpc.net/problem/2374)

There is an array A of length N.
If you perform Add(i), the i-th element and its adjacent elements with the same value will increase by 1.
Determine the minimum number of Add() operations to make all elements identical.
'''

# TIME COMPLEXITY : O(N^2)

import sys
inf = float('inf')


# 1. TO GET THE INPUT

length = int(sys.stdin.readline())

arr = []
for element in range(length):
    arr.append(int(sys.stdin.readline()))


# 2. TO SOLVE THE PROBLEM
# Perform 'Add' operation to the minimum element.

ans = 0
now_length = length

while now_length != 1:
    
    # Find the minimum element
    
    min_val = inf
    min_idx = -1
    
    for idx in range(now_length):
        if arr[idx] < min_val:
            min_val = arr[idx]
            min_idx = idx
    
    # Perform 'Add' operation
    
    if min_idx == 0:
        ans += arr[min_idx+1] - arr[min_idx]
    elif min_idx == now_length - 1:
        ans += arr[min_idx-1] - arr[min_idx]
    else:
        ans += min(arr[min_idx+1] - arr[min_idx], arr[min_idx-1] - arr[min_idx])
    
    arr.pop(min_idx)
    now_length -= 1

print(ans)