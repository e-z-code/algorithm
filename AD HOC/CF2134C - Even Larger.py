'''
CF2134C - Even Larger (https://codeforces.com/contest/2134/problem/C)

An array is called good if, for every sub-array, the sum of the elements at even indices (with respect to the original array) is not less than the sum of the elements at odd indices.
You are given an array A of N non-negative integers.
In one operation, you can decrease any element in the array by 1.
Find the minimum number of operations needed to make the array A good.
'''

# TIME COMPLEXITY : O(N)

import sys


# 1. TO GET THE INPUT

test_count = int(sys.stdin.readline())

for test in range(test_count):
    
    length = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    
    
    # 2. TO SOLVE THE PROBLEM
    
    ans = 0
    for idx in range(0, length, 2):
        if idx == 0:
            op_count = max(arr[idx] - arr[idx+1], 0)
            arr[idx] -= op_count
        else:
            if idx == length - 1:
                op_count = max(arr[idx] - arr[idx-1], 0)
            else:
                op_count = max(arr[idx] - arr[idx+1], arr[idx] - arr[idx-1], 0)
            arr[idx] -= op_count
            if arr[idx-2] + arr[idx] > arr[idx-1]:
                add_count = arr[idx-2] + arr[idx] - arr[idx-1]
                arr[idx] = max(0, arr[idx] - add_count)
                op_count += add_count
        ans += op_count
    
    print(ans)