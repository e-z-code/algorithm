'''
BOJ3362 - Riddles (https://www.acmicpc.net/problem/3361)

There are N coins in the order of A1, A2, ..., An.
The goal is to pay all prices from 1 to K with the first X coins.
What is the minimum value of X?
'''

# TIME COMPLEXITY : O(TN log ^ 2 N)

import sys


# 2. FUNCTION TO SOLVE DECISION PROBLEM
# Given X, is it possible to pay all prices from 1 to N with first X coins?

def possible(coins):
    
    coins = sorted(coins)
    max_possible = 0
    
    for coin in coins:
        if max_possible + 1 < coin:
            return False
        else:
            max_possible += coin
    
    if price_count <= max_possible:
        return True
    else:
        return False


# 1. TO GET THE INPUT

test_count = int(sys.stdin.readline())

for test in range(test_count):
    
    coin_count, price_count = map(int, sys.stdin.readline().split())
    coins = list(map(int, sys.stdin.readline().split()))
    
    
    # 3. PARAMETRIC SEARCH
    
    if not possible(coins):
        
        print(-1)
    
    else:
        
        left = 1
        right = coin_count
        
        while left + 1 < right:
            
            mid = (left + right) // 2
            if possible(coins[:mid]):
                right = mid
            else:
                left = mid
        
        print(right)