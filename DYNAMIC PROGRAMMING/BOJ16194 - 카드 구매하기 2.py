'''
BOJ16194 - Card Purchase 2 (https://www.acmicpc.net/problem/16194)

There are N cards.
You can buy a card, two cards, and so on at different price.
Determine the minimum price to buy N cards.
'''

# TIME COMPLEXITY : O(N^2)


import sys
inf = float('inf')


# 1. TO GET THE INPUT

card_count = int(sys.stdin.readline())
prices = [0] + list(map(int, sys.stdin.readline().split()))


# 2. DP

dp = [inf for count in range(card_count + 1)]
dp[0] = 0

for now_count in range(1, card_count + 1):
    for count in range(1, now_count + 1):
        dp[now_count] = min(dp[now_count], dp[now_count - count] + prices[count])

print(dp[-1])