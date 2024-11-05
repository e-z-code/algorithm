'''
BOJ12920 - Knapsack 2 (https://www.acmicpc.net/problem/12920)

There are N items.
You are given the amount and the value of each item and the capacity of the knapsack.
Determine the maximum value you can put in the knapsack.
'''

# TIME COMPLEXITY : O(NM log M)

import sys


# 1. TO GET THE INPUT

item_count, capacity = map(int, sys.stdin.readline().split())

items = []
for item in range(item_count):
    
    weight, value, count = map(int, sys.stdin.readline().split())
    
    # Bundle multiple (exponent of 2) items to represent every quantity
    # (e.g.) 7 items = 4 items + 2 items + 1 item
    quantity = 1
    while quantity <= count:
        items.append((weight * quantity, value * quantity))
        count -= quantity
        quantity *= 2
    
    # The remainders also have to be bundled
    if count != 0:
        items.append((weight * count, value * count))


# 2. KNAPSACK DP
# dp[i][j] = Maximum value when considering first i items and the capacity of knapsack equals j

dp = [[0 for j in range(capacity + 1)] for i in range(len(items) + 1)]

for i in range(1, len(items) + 1):
    
    weight, value = items[i-1]
    
    for j in range(1, capacity + 1):
        if weight <= j:
            dp[i][j] = max(dp[i-1][j-weight] + value, dp[i-1][j]) # To put the item or not
        else:
            dp[i][j] = dp[i-1][j]

print(dp[-1][-1])