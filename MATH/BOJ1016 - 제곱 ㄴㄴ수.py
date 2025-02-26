'''
BOJ1016 - No Square Numbers (https://www.acmicpc.net/problem/1016)

NSN [No Square Numbers] is a number that is not divisible by any squared numbers except for 1.
Given A and B, determine the number of NSNs between A and B.
'''

# TIME COMPLEXITY : O(X log X) [X = sqrt(N)]

import sys


# 1. TO FIND PRIME NUMBERS

prime = [1 for idx in range(1000001)]
prime[0], prime[1] = 0, 0

divisor = 2

while divisor <= 1000:
    if prime[divisor]:
        for multiple in range(divisor * 2, 1000001, divisor):
            prime[multiple] = 0
    divisor += 1

prime_nums = []
for num in range(1000001):
    if prime[num]:
        prime_nums.append(num)


# 2. TO SOLVE THE PROBLEM

lowest, highest = map(int, sys.stdin.readline().split())

OFFSET = lowest
ans = [1 for num in range(highest - lowest + 1)]

for prime_num in prime_nums:
    
    divisor = prime_num * prime_num
    
    if lowest % divisor == 0:
        start = lowest - OFFSET
    else:
        start = lowest + divisor - lowest % divisor - OFFSET
    
    for multiple in range(start, len(ans), divisor):
        ans[multiple] = 0

print(sum(ans))