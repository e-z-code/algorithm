'''
BOJ12903 - Painting Balls (https://www.acmicpc.net/problem/12903)

There are N balls with K colors numbered from 1 to K.
You arrange the balls in a row.
The arrangement is valid if the last X always appears earlier than the last X+1 for all X.
Determine the possible number of valid arrangements.
'''

# TIME COMPLEXITY : O(max(K, N))

import sys
MOD = 10 ** 9 + 7


# 3. FACTORIAL

factorial = [1]
for num in range(1, 1001):
    factorial.append(factorial[-1] * num)


# 1. TO GET THE INPUT

color_count = int(sys.stdin.readline())

ball_count = []
for color in range(color_count):
    ball_count.append(int(sys.stdin.readline()))


# 2. PREFIX SUM

prefix_sum = [ball_count[0]]
for color in range(1, color_count):
    prefix_sum.append(prefix_sum[-1] + ball_count[color])


# 4. DP
# DP[i] = The number of cases when considering until i-th color.
# If B[X] is the number of balls of color X, DP[i] = DP[i-1] X C(B[1] + ... + B[i] - 1, B[i] - 1)

dp = [0 for color in range(color_count)]
dp[0] = 1

for color in range(1, color_count):
    
    dp[color] = dp[color-1] * (factorial[prefix_sum[color] - 1] // (factorial[ball_count[color] - 1] * factorial[prefix_sum[color] - ball_count[color]]))
    dp[color] %= MOD

print(dp[-1])