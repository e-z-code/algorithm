'''
CF2132C2 - The Cunning Seller [Hard] (https://codeforces.com/contest/2132/problem/C2)

You can buy pow(3, X) watermelons for (9 + X) * pow(3, X - 1) coins.
You want to buy N watermelons with no more than K deals.
Determine the minimum number of coins you must pay.
'''

# TIME COMPLEXITY : O(T log N)

import sys


# 1. TO GET THE INPUT

test_count = int(sys.stdin.readline())

for test in range(test_count):
    
    watermelon_count, deal_count = map(int, sys.stdin.readline().split())
    
    
    # 2. TO GET THE MINIMUM NUMBER OF OPERATIONS
    
    exp_count = [0 for idx in range(20)]
    
    exp = 19
    while exp >= 0:
        if pow(3, exp) <= watermelon_count:
            exp_count[exp] += 1 
            watermelon_count -= pow(3, exp)
        else:
            exp -= 1
    
    
    # 3. TO SOLVE THE PROBLEM
    
    if sum(exp_count) > deal_count:
        
        print(-1)
    
    else:
        
        deal_count -= sum(exp_count)
        
        # It is always better to make 3 small deals than 1 large deal.
        now_exp = 19
        for exp in range(19, 0, -1):
            swap_count = min(deal_count // 2, exp_count[exp])
            exp_count[exp] -= swap_count
            exp_count[exp-1] += swap_count * 3
            deal_count -= swap_count * 2
        
        ans = 0
        for exp in range(20):
            ans += (9 + exp) * pow(3, exp - 1) * exp_count[exp]
        print(int(ans))