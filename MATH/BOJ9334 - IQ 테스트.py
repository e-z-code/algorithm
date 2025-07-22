'''
BOJ9334 - IQ Test (https://www.acmicpc.net/problem/9334)

You are given a sequence A.
It satisfies a recurrence relation of the form A[i] = X[1] * A[i-1] + ... + X[D] * A[i-D] when D <= 3 and all elements of X are integers.
Find the next term of the sequence.
If there are multiple possible answers, prefer one with a smaller D.
'''

# TIME COMPLEXITY : O(T|A|)

import sys
from fractions import Fraction


# 1. TO GET THE INPUT

test_count = int(sys.stdin.readline())

for test in range(test_count):
    
    arr = list(map(int, sys.stdin.readline().split()))[1:]
    length = len(arr)
    
    
    # 2. TO SOLVE THE PROBLEM
    # To find valid index to calculate coefficients, calculate coefficients, and find the next term.
    
    # D = 1
    
    key_idx = 0
    for idx in range(length - 1):
        P_denominator = arr[idx]
        if P_denominator != 0:
            key_idx = idx
            break
        
    P = Fraction(arr[key_idx+1], arr[key_idx+0])
    
    check = True
    for idx in range(1, length):
        if arr[idx-1] * P != arr[idx]:
            check = False
            break
    
    if check:
        print(arr[-1] * P)
        continue
    
    # D = 2
    
    key_idx = 0
    for idx in range(length - 3):
        Q_denominator = arr[idx] * arr[idx+2] - arr[idx+1] * arr[idx+1]
        P_denominator = arr[idx+1]
        if Q_denominator != 0 and P_denominator != 0:
            key_idx = idx
            break
    
    Q = Fraction(arr[key_idx+2] * arr[key_idx+2] - arr[key_idx+1] * arr[key_idx+3], arr[key_idx+0] * arr[key_idx+2] - arr[key_idx+1] * arr[key_idx+1])
    P = Fraction(arr[key_idx+2] - Q * arr[key_idx+0], arr[key_idx+1])
    
    check = True
    for idx in range(2, length):
        if arr[idx-1] * P + arr[idx-2] * Q != arr[idx]:
            check = False
            break
    
    if check:
        print(arr[-1] * P + arr[-2] * Q)
        continue
    
    # D = 3
    
    key_idx = 0
    for idx in range(length - 3):
        R_denominator = (arr[idx] * arr[idx+3] - arr[idx+1] * arr[idx+2]) * (arr[idx+2] * arr[idx+4] - arr[idx+3] * arr[idx+3]) - (arr[idx+1] * arr[idx+4] - arr[idx+2] * arr[idx+3]) * (arr[idx+1] * arr[idx+3] - arr[idx+2] * arr[idx+2])
        Q_denominator = arr[idx+1] * arr[idx+3] - arr[idx+2] * arr[idx+2]
        P_denominator = arr[idx+2]
        if R_denominator != 0 and Q_denominator != 0 and P_denominator != 0:
            key_idx = idx
            break
    
    R = Fraction((arr[key_idx+3] * arr[key_idx+3] - arr[key_idx+2] * arr[key_idx+4]) * (arr[key_idx+2] * arr[key_idx+4] - arr[key_idx+3] * arr[key_idx+3]) - (arr[key_idx+4] * arr[key_idx+4] - arr[key_idx+3] * arr[key_idx+5]) * (arr[key_idx+1] * arr[key_idx+3] - arr[key_idx+2] * arr[key_idx+2]), (arr[key_idx+0] * arr[key_idx+3] - arr[key_idx+1] * arr[key_idx+2]) * (arr[key_idx+2] * arr[key_idx+4] - arr[key_idx+3] * arr[key_idx+3]) - (arr[key_idx+1] * arr[key_idx+4] - arr[key_idx+2] * arr[key_idx+3]) * (arr[key_idx+1] * arr[key_idx+3] - arr[key_idx+2] * arr[key_idx+2]))
    Q = Fraction(arr[key_idx+3] * arr[key_idx+3] - arr[key_idx+2] * arr[key_idx+4] - R * (arr[key_idx+0] * arr[key_idx+3] - arr[key_idx+1] * arr[key_idx+2]), arr[key_idx+1] * arr[key_idx+3] - arr[key_idx+2] * arr[key_idx+2])
    P = Fraction(arr[key_idx+3] - Q * arr[key_idx+1] - R * arr[key_idx+0], arr[key_idx+2])
    
    check = True
    for idx in range(3, length):
        if arr[idx-1] * P + arr[idx-2] * Q + arr[idx-3] * R != arr[idx]:
            check = False
            break
    
    if check:
        print(arr[-1] * P + arr[-2] * Q + arr[-3] * R)