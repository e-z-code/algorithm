'''
CF2132C1 - The Cunning Seller [Easy] (https://codeforces.com/contest/2132/problem/C1)

You can buy pow(3, X) watermelons for (9 + X) * pow(3, X - 1) coins.
You want to buy N watermelons with the minimum number of deals.
Determine the minimum number of coins you must pay.
'''

# TIME COMPLEXITY : O(T log N)

import sys


# 1. TO GET THE INPUT

test_count = int(sys.stdin.readline())

for test in range(test_count):
    
    watermelon_count = int(sys.stdin.readline())
    
    
    # 2. TO SOLVE THE PROBLEM
    
    ans = 0
    exp = 19
    while exp >= 0:
        if pow(3, exp) <= watermelon_count:
            ans += (9 + exp) * pow(3, exp - 1)
            watermelon_count -= pow(3, exp)
        else:
            exp -= 1
    
    print(int(ans))