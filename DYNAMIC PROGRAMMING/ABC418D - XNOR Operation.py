'''
ABC418D - XNOR Operation (https://atcoder.jp/contests/abc418/tasks/abc418_d)

A non-empty binary string S is a beautiful string when it satisfies the following condition.

You can perform the following sequence of operations until S = 1.
(1) Choose i such that 1 <= i <= |S| - 1.
(2) If S[i] == S[i+1], let X = 1. Otherwise, let X = 0.
(3) Replace S[i] and S[i+1] with X.

Given a binary string T of length N, find the number of beautiful substrings of T.
'''

# TIME COMPLEXITY: O(N)

import sys


# 1. TO GET THE INPUT

length = int(sys.stdin.readline())
string = sys.stdin.readline().strip()


# 2. DP

dp = [[0, 0] for idx in range(length)]

if string[0] == "0":
    dp[0][0] = 1
else:
    dp[0][1] = 1

for idx in range(1, length):
    
    if string[idx] == "0":
        dp[idx][0] = dp[idx-1][1] + 1
        dp[idx][1] = dp[idx-1][0]
    else:
        dp[idx][0] = dp[idx-1][0]
        dp[idx][1] = dp[idx-1][1] + 1


# 3. TO SOLVE THE PROBLEM

ans = 0
for idx in range(length):
    ans += dp[idx][1]
print(ans)