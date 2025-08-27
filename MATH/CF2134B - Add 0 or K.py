'''
CF2134B - Add 0 or K (https://codeforces.com/contest/2134/problem/B)

There is an array A of length N and a positive integer K.
In one operation, you may add either 0 or K to each element of A.
Perform at must K such operations to make gcd(A) > 1.
'''

# TIME COMPLEXITY : O(N)

import sys


# 1. TO GET THE INPUT

test_count = int(sys.stdin.readline())

for test in range(test_count):
    
    length, val = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))
    
    
    # 2. TO SOLVE THE PROBLEM
    # If you add K to an element, its mod (K+1) value decreases by 1.
    
    for idx in range(length):
        
        now_mod = arr[idx] % (val + 1)
        arr[idx] += now_mod * val
    
    print(" ".join(map(str, arr)))