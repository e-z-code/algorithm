'''
BOJ6913 - Constrained Permutations (https://www.acmicpc.net/problem/6913)

Determine the number of permutations which satisfy all constraints.
A constraint is a pair (x, y) indicating that x must come before y in the permutation.
'''

# TIME COMPLEXITY : O(N! X max(N, K))

import sys
from itertools import permutations


# 1. TO GET THE INPUT

size = int(sys.stdin.readline())
constraint_count = int(sys.stdin.readline())

constraints = []
for constraint in range(constraint_count):
    x, y = map(int, sys.stdin.readline().split())
    constraints.append((x, y))


# 2. TO SOLVE THE PROBLEM (BRUTE-FORCE)

ans = 0

for permutation in permutations(range(1, size + 1)):
    
    loc = [0 for num in range(size + 1)]
    
    for idx in range(size):
        loc[permutation[idx]] = idx
    
    valid = True
    
    for constraint in constraints:
        before, after = constraint
        if loc[before] > loc[after]:
            valid = False
            break
    
    if valid:
        ans += 1

print(ans)