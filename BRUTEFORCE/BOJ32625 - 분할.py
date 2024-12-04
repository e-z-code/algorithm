'''
BOJ32625 - Partition (https://www.acmicpc.net/problem/32625)

There is an array A of length N.
Determine if it is possible to divide the array into X substrings of length L such that:

(1) All elements belong to one substring.
(2) L is the same for all substrings, and 1 <= L < N.
(3) The sum of max(X) + min(X) is same for all X. 
'''

# TIME COMPLEXITY : O(N X D(N)) [D(N) = The number of divisors of N]
# Given N <= 100000, the maximum value of N X D(N) = 12579840 when N = 83160

import sys


# 1. TO GET THE INPUT

length = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))


# 2. TO GET ALL DIVISORS
# The length of substrings must be a divisor of N.

possible_length = []

for divisor in range(1, length):
    if length % divisor == 0:
        possible_length.append(divisor)


# 3. TO SOLVE THE PROBLEM

possible = 0

for sub_length in possible_length:
    
    check = None
    
    for start in range(0, length, sub_length):
        
        sub_arr = arr[start:start+sub_length]
        val = min(sub_arr) + max(sub_arr)
        
        if check == None:
            check = val
        else:
            if check != val:
                break
            else:
                if start == length - sub_length:
                    possible = 1

print(possible)