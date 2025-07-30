'''
BOJ14543 - Linear Equation (https://www.acmicpc.net/problem/14543)

Solve the equation Ax + B = C.
'''

# TIME COMPLEXITY : O(1)

import sys


# 1. TO GET THE INPUT

equation_count = int(sys.stdin.readline())

for equation_num in range(1, equation_count + 1):
    
    equation = list(sys.stdin.readline().strip().split())
    
    
    # 2. TO SOLVE THE PROBLEM
    
    A, B, C = int(equation[0][:-1]), int(equation[2]), int(equation[4])
    
    if A == 0:
        if B == C:
            ans = "More than one solution."
        else:
            ans = "No solution."
    else:
        val = (C - B) / A
        val = int(val * 1000000) / 1000000
        ans = "x = {}".format(format(val, ".6f"))
    
    print("Equation {}".format(equation_num))
    print(ans)
    print()