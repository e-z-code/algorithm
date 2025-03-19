'''
BOJ1887 - Lucky Ticket (https://www.acmicpc.net/problem/13231)

Find the number of 2N-digit numbers such that the sum of the first N digits and that of the last N digits are equal.
'''

# TIME COMPLEXITY : O(TN^2)

import sys
MOD = pow(10, 9) + 7


# 1. DP
# DP[i][j] = The number of cases when the sum of i digits equal j.

dp = [[0 for digit_sum in range(5001)] for digit in range(501)]
    
for now_digit in range(10):
    dp[1][now_digit] = 1
    
for digit in range(2, 501):
    for digit_sum in range(5001):
            
        for now_digit in range(10):
            if digit_sum >= now_digit:
                dp[digit][digit_sum] += dp[digit-1][digit_sum-now_digit]
        dp[digit][digit_sum] %= MOD


# 2. TO GET THE INPUT

test_count = int(sys.stdin.readline())

for test in range(1, test_count + 1):
    
    digit_count = int(sys.stdin.readline())
    
    
    # 3. TO SOLVE THE PROBLEM
    
    ans = 0
    
    for digit_sum in range(5001):
        ans += pow(dp[digit_count][digit_sum], 2)
        ans %= MOD 

    print("Case #{}: {}".format(test, ans))