'''
BOJ18858 - Way to Boot Camp (https://www.acmicpc.net/problem/18858)

A non-mountain sequence is a sequence that satisfies the following condition.

- For every 2 <= i < N, "A[i-1] < A[i] and A[i] > A[i+1]" does not hold.

You want to make a sequence of length N using numbers from 1 to M.
Determine the number of non-mountain sequence you can make.
'''

# TIME COMPLEXITY : O(NM^2)


import sys
mod = 998244353


# 1. TO GET THE INPUT

arr_length, max_num = map(int, sys.stdin.readline().split())


# 2. DYNAMIC PROGRAMMING
# dp[L][J][X] = (The number of non-mountain array of length L that ends with J when X indicates if the array ended in ascent, descent, or neither.)

dp = [[[0, 0, 0] for last_num in range(max_num + 1)] for length in range(arr_length + 1)]

for length in range(1, arr_length + 1):
    for last_num in range(1, max_num + 1):
        
        if length == 1:
            dp[length][last_num][1] = 1
        else:
            # End in ascent
            for before_num in range(1, last_num):
                dp[length][last_num][0] += sum(dp[length-1][before_num])
                dp[length][last_num][0] %= mod
            # End in same
            dp[length][last_num][1] += sum(dp[length-1][last_num])
            dp[length][last_num][1] %= mod
            # End in descent
            for before_num in range(last_num + 1, max_num + 1):
                dp[length][last_num][2] += dp[length-1][before_num][1] + dp[length-1][before_num][2]
                dp[length][last_num][2] %= mod


# 3. TO SOLVE THE PROBLEM

ans = 0

for last_num in range(1, max_num + 1):
    ans += sum(dp[arr_length][last_num])
    ans %= mod

print(ans)