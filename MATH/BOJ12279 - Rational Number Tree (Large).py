'''
BOJ12279 - Rational Number Tree (Large) (https://www.acmicpc.net/problem/12279)

There is a complete binary tree.
The root node is 1/1, and the left and right children of node P/Q are P/(P+Q) and (P+Q)/Q.

Answer two kinds of queries.
(1) Find the N-th element of the array.
(2) Given P/Q, find its position in the array.
'''

# TIME COMPLEXITY : O(log N)

import sys


# 1. TO GET THE INPUT

test_count = int(sys.stdin.readline())

for test in range(1, test_count + 1):
    
    query = list(map(int, sys.stdin.readline().split()))
    
    
    # 2. QUERY 1 - FIND A NUMBER GIVEN INDEX
    # If an index is an even number, the element is a left child.
    # Otherwise, the element is a right child.
    
    if query[0] == 1:
    
        idx = query[1]
        
        moves = []
        while idx != 1:
            if idx % 2 == 0:
                moves.append("L")
            else:
                moves.append("R")
            idx >>= 1
        
        ans_numerator = 1
        ans_denominator = 1
        
        while moves:
            op = moves.pop()
            if op == "L":
                ans_numerator, ans_denominator = ans_numerator, ans_numerator + ans_denominator
            else:
                ans_numerator, ans_denominator = ans_numerator + ans_denominator, ans_denominator
        
        print("Case #{}: {} {}".format(test, ans_numerator, ans_denominator))
    
    
    # 3. QUERY 2 - FIND AN INDEX GIVEN NUMBER
    # If a numerator is smaller than denominator, it is left child.
    # Otherwise, it is right child.
    
    else:
        
        numerator, denominator = query[1], query[2]
        
        moves = []
        while numerator != 1 or denominator != 1:
            if numerator < denominator:
                moves.append("L")
                numerator, denominator = numerator, denominator - numerator
            else:
                moves.append("R")
                numerator, denominator = numerator - denominator, denominator
        
        ans = 1
        while moves:
            op = moves.pop()
            if op == "L":
                ans = ans * 2
            else:
                ans = ans * 2 + 1

        print("Case #{}: {}".format(test, ans))