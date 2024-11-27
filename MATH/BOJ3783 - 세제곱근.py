'''
BOJ3783 - Cube root (https://www.acmicpc.net/problem/3783)

Given a number, determine its cube root.
'''

# TIME COMPLEXITY : O(T)

import sys
from decimal import *

getcontext().prec = 1000 # To increase precision of Decimal objects.


# 1. TO GET THE INPUT

test_count = int(sys.stdin.readline())

for test in range(test_count):
    
    
    # 2. TO SOLVE THE PROBLEM
    
    num = Decimal(sys.stdin.readline().strip())
    a_third = Decimal('1') / Decimal('3')
    
    ans = num ** a_third
    ans = round(ans, 500) # To fix tiny errors
    print(ans.quantize(Decimal('.0000000001'), rounding=ROUND_FLOOR)) # To print 10 decimal places