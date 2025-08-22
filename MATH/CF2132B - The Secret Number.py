'''
CF2132B - The Secret Number (https://codeforces.com/contest/2132/problem/B)

You are given X.
You appended a positive number of zeros to the right of it, thus obtaining an new number Y.
Then, you obtained N = X + Y.
Given N, find all suitable X.
'''

# TIME COMPLEXITY : O(T log N)


import sys


# 1. TO GET THE INPUT AND SOLVE THE PROBLEM

divisors = [pow(10, exp) + 1 for exp in range(1, 20)]

test_count = int(sys.stdin.readline())

for test in range(test_count):
    
    num = int(sys.stdin.readline())
    
    ans = []
    for divisor in divisors:
        if num % divisor == 0:
            ans.append(str(num // divisor))

    if len(ans) == 0:
        print(len(ans))
    else:
        print(len(ans))
        for idx in range(len(ans) - 1, -1, -1):
            print(ans[idx], end = ' ')
        print()