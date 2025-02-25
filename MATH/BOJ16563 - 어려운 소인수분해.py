'''
BOJ16563 - Difficult Factorization (https://www.acmicpc.net/problem/16563)

Factorize N integers.
'''

# TIME COMPLEXITY : O(X log X) [X : Maximum value]

import sys 


# 1. TO FIND PRIME NUMBERS

is_prime = [1 for num in range(5000001)]
is_prime[0], is_prime[1] = 0, 0

divisor = 2
while divisor <= 2250:
    if is_prime[divisor]:
        for multiple in range(divisor * 2, 5000001, divisor):
            is_prime[multiple] = 0
    divisor += 1

prime_nums = []
for num in range(5000001):
    if is_prime[num]:
        prime_nums.append(num)


# 2. TO GET THE INPUT

query_count = int(sys.stdin.readline())
queries = list(map(int, sys.stdin.readline().split()))


# 3. TO SOLVE THE PROBLEM

for query in queries:
    
    now = query
    for prime_num in prime_nums:
        
        while now % prime_num == 0:
            print(prime_num, end = ' ')
            now //= prime_num
        
        if now == 1:
            print()
            break
        elif is_prime[now]:
            print(now, end = ' ')
            print()
            break
