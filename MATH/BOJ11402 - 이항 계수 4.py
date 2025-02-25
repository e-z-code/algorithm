'''
BOJ11402 - Binomial Coefficient 4 (https://www.acmicpc.net/problem/11402)

Calculate C(N, K) % M.
M is a prime number.
'''

# TIME COMPLEXITY : O(M^2)

import sys


# 1. TO GET THE INPUT

n, k, p = map(int, sys.stdin.readline().split())


# 2. TO GET THE COMBINATION VALUES

combination = [[0 for j in range(2001)] for i in range(2001)]

for i in range(2001):
    combination[i][0] = 1
    combination[i][i] = 1

for i in range(2, 2001):
    for j in range(1, i):
        combination[i][j] = combination[i-1][j-1] + combination[i-1][j]
        combination[i][j] %= p


# 3. TO SOLVE THE PROBLEM - LUCAS THEOREM

p_base_n = []
p_base_k = []

divisor = 1
while divisor * p <= n:
    divisor *= p

while divisor != 0:
    
    p_base_n.append(n // divisor)
    n %= divisor
    
    p_base_k.append(k // divisor)
    k %= divisor
    
    divisor //= p

ans = 1

for idx in range(len(p_base_n)):
    ans *= combination[p_base_n[idx]][p_base_k[idx]]
    ans %= p

print(ans)