'''
BOJ14881 - Water Bottle Problem (https://www.acmicpc.net/problem/14881)

There are two bottles with a capacity of A liters and B liters, respectively.
Determine if you can make water of C liters.
'''

# TIME COMPLEXITY : O(T log max(A, B)) [T : Number of test cases]

import sys
from math import gcd


# 1. TO GET THE INPUT

test_count = int(sys.stdin.readline())

for test in range(test_count):
    
    sizeA, sizeB, goal = map(int, sys.stdin.readline().split())
    
    
    # 2. TO SOLVE THE PROBLEM
    # Bezout's Identity can be applied.
    
    possible = True
    if goal > max(sizeA, sizeB):
        possible = False
    if goal % gcd(sizeA, sizeB) != 0:
        possible = False
    
    if possible:
        print("YES")
    else:
        print("NO")