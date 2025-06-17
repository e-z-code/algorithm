'''
BOJ12014 - Stock (https://www.acmicpc.net/problem/12014)

You can buy a stock in K days for next N days.
You know the price for next N days.
Determine if you can buy stocks such that the price is always increasing.
'''

# TIME COMPLEXITY : O(TN^2)

import sys


# 1. TO GET THE INPUT

test_count = int(sys.stdin.readline())

for test_num in range(1, test_count + 1):
    
    day_count, goal_length = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))
    
    
    # 2. TO SOLVE THE PROBLEM
    # The problem is equivalent to see if the length of the LIS is shorter than K or not.
    
    dp = [1 for idx in range(day_count)]
    
    for i in range(1, day_count):
        for j in range(i):
            if arr[i] > arr[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
    
    print("Case #{}".format(test_num))
    if max(dp) >= goal_length:
        print(1)
    else:
        print(0)