'''
BOJ27690 - Boredom Buster [Easy] (https://www.acmicpc.net/problem/27690)

You can split the number X into two parts, Y and Z, such that X = Y + Z.
After performing a split, you will get a score of YZ.
You can repeat the operations until only 1s are left.
Determine the maximum score you can get.

However, in this problem, there is exactly one way of splitting.
(1) If X % 3 = 0, then Y = X / 3.
(2) Else if X % 2 = 0, then Y = X / 2.
(3) Otherwise, then Y = 1.
'''

# TIME COMPLEXITY : O(N)

import sys


# 1. PRE-PROCESSING

ans = [0 for num in range(1000001)]

for num in range(2, 1000001):
    
    if num % 3 == 0:
        numA, numB = num // 3, num // 3 * 2 
    elif num % 2 == 0:
        numA, numB = num // 2, num // 2
    else:
        numA, numB = 1, num - 1
    
    ans[num] = ans[numA] + ans[numB] + numA * numB


# 2. TO GET THE INPUT AND SOLVE THE PROBLEM

test_count = int(sys.stdin.readline())

for test in range(test_count):
    
    blank = sys.stdin.readline().strip()
    num = int(sys.stdin.readline())
    
    print(ans[num])