'''
BOJ9569 - No Change (https://www.acmicpc.net/problem/9569)

You want to make a sequence of N purchases with K coins.
You can periodically stop and pay, with a single coin, for all the purchases made since the last payment.
Unfortunately, the vendors are completely out of change.
Determine the maximum amount of money you can end up.
'''

# TIME COMPLEXITY : O(2^K * K log N)

import sys
from bisect import bisect_right


# 1. TO GET THE INPUT

coin_count, buy_count = map(int, sys.stdin.readline().split())

coins = []
for coin in range(coin_count):
    coins.append(int(sys.stdin.readline()))

prefix_sum = []
for buy in range(buy_count):
    if len(prefix_sum) == 0:
        prefix_sum.append(int(sys.stdin.readline()))
    else:
        prefix_sum.append(prefix_sum[-1] + int(sys.stdin.readline()))


# 2. DP

dp = [0 for case in range(1 << coin_count)]

for case in range(1, 1 << coin_count):
    for coin in range(coin_count):
        
        if case & (1 << coin):
            last_case = case ^ (1 << coin)
            max_purchase = bisect_right(prefix_sum, dp[last_case] + coins[coin])
            if max_purchase != 0:
                dp[case] = max(dp[case], prefix_sum[max_purchase - 1])


# 3. TO SOLVE THE PROBLEM

ans = -1

for case in range(1 << coin_count):
    if dp[case] == prefix_sum[-1]:
        
        left = 0
        for coin in range(coin_count):
            if not (case & (1 << coin)):
                left += coins[coin]
        ans = max(left, ans)

print(ans)