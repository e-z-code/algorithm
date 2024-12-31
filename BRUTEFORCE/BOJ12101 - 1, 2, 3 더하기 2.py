'''
BOJ12101 - 1, 2, 3 Addition 2 (https://www.acmicpc.net/problem/12101)

An addition is valid if it only consists of the addition of 1, 2, and 3.
Given N, find the K-th possible valid addition in lexicographical order.
'''

# TIME COMPLEXITY : O(N X pow(3, N))

import sys
from collections import deque


# 1. TO GET THE INPUT

result, order = map(int, sys.stdin.readline().split())
order -= 1


# 2. TO FIND VALID ADDITIONS

queue = deque([[]])
valid = []

while queue:
    
    now = queue.pop()
    now_sum = sum(now)
    
    if now_sum == result:
        valid.append(now)
    else:
        if now_sum + 1 <= result:
            next = now[:]
            next.append(1)
            queue.append(next)
        if now_sum + 2 <= result:
            next = now[:]
            next.append(2)
            queue.append(next)
        if now_sum + 3 <= result:
            next = now[:]
            next.append(3)
            queue.append(next)


# 3. TO SOLVE THE PROBLEM

valid.sort()

if len(valid) <= order:
    print(-1)
else:
    print("+".join(map(str, valid[order])))