'''
BOJ1887 - Cow Pizza (https://www.acmicpc.net/problem/1887)

There are T different toppings and N invalid constraints.
Determine the number of valid combinations.
'''

# TIME COMPLEXITY : O(pow(2, T) X N)

import sys


# 1. TO GET THE INPUT

topping_count, constraint_count = map(int, sys.stdin.readline().split())

constraints = []
for constraint_num in range(constraint_count):
    
    key = 0
    constraint = list(map(int, sys.stdin.readline().split()))[1:]
    
    for topping in constraint:
        key |= (1 << (topping-1))
    
    constraints.append(key)


# 2. BRUTE-FORCING

ans = 0

for combination in range(1 << topping_count):
    
    valid = True
    for constraint in constraints:
        if combination & constraint == constraint:
            valid = False
            break
    
    if valid:
        ans += 1

print(ans)