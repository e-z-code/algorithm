'''
BOJ26073 - Candy Distribution (https://www.acmicpc.net/problem/3955)

Given C and K, find (X, Y) such that KX + 1 = CY.
'''

# TIME COMPLEXITY : O(T log max(C, K)) [T : Number of test cases]

import sys
from math import gcd
MAX = pow(10, 9)


# 2. EXTENDED EUCLIDEAN
# The function finds (A, B) for Ax + By = gcd(x, y)

def extended_euclidean(x, y):
    
    A_for_x, A_for_y = 1, 0
    B_for_x, B_for_y = 0, 1
    
    while y != 0:
    
        quotient = x // y
        remainder = x - (y * quotient)
        
        x, y = y, remainder
        A_for_x, A_for_y = A_for_y, A_for_x - A_for_y * quotient
        B_for_x, B_for_y = B_for_y, B_for_x - B_for_y * quotient
    
    return A_for_x, B_for_x


# 1. TO GET THE INPUT

test_count = int(sys.stdin.readline())

for test in range(test_count):
    
    people_count, candy_count = map(int, sys.stdin.readline().split())
    
    
    # 3. TO SOLVE THE PROBLEM
    # The problem is equivalent to find (X, Y) such that CX - KY = 1
    # According to Bezout's identity, gcd(C, K) must be 1.
    
    if gcd(candy_count, people_count) != 1:
        
        print("IMPOSSIBLE")
        
    else:
        
        if candy_count >= people_count:
            buy_count, candy_for_people = extended_euclidean(candy_count, people_count)
        else:
            candy_for_people, buy_count = extended_euclidean(people_count, candy_count)
        candy_for_people *= -1
        
        # Be aware that 0 < X <= MAX and 0 < Y.  
        
        if candy_for_people < 0:
            move = abs(candy_for_people) // candy_count + 1
            candy_for_people += move * candy_count
            buy_count += move * people_count
        else:
            move = candy_for_people // candy_count
            if candy_for_people % candy_count == 0:
                move -= 1
            candy_for_people -= move * candy_count
            buy_count -= move * people_count
        
        if buy_count > MAX:
            print("IMPOSSIBLE")
        else:
            print(buy_count)