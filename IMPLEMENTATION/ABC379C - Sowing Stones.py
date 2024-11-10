'''
ABC379C - Sowing Stones (https://atcoder.jp/contests/abc379/tasks/abc379_c)

There are N cells numbered from 1 to N in a row.
You can perform the following operation any number of times: Move one stone from cell i to cell i+1.
Given an initial state, determine if it is possible to reach a state where all cells contain exactly one stone.
If so, find the minimum number of operations required to reach the state.
'''

# TIME COMPLEXITY : O(M)

import sys


# 1. TO GET THE INPUT

length, occupied_count = map(int, sys.stdin.readline().split())

occupied_cells = list(map(int, sys.stdin.readline().split()))
occupied_stones = list(map(int, sys.stdin.readline().split()))

# To the setter: I highly recommend providing such input in a sorted order or at least sample input in an unsorted order.

occupied_info = []
for idx in range(occupied_count):
    occupied_info.append([occupied_cells[idx], occupied_stones[idx]])
occupied_info.sort() 

if occupied_info[-1][0] != length:
    occupied_info.append([length, 0])


# 2. TO SOLVE THE PROBLEM
# To "spread" stones from the left

ans = 0

for idx in range(len(occupied_info) - 1):
    
    now_cell, now_stones = occupied_info[idx]
    next_cell = occupied_info[idx+1][0]
    
    # The process must start at cell 1
    if idx == 0 and now_cell != 1:
        ans = -1
        break

    distance = next_cell - now_cell
    # The spread must reach the next occupied cell
    if now_stones < distance:
        ans = -1
        break
    else:
        ans += (distance - 1) * distance // 2
        ans += (now_stones - distance) * distance
        occupied_info[idx+1][1] += now_stones - distance

# The cell N must contain exactly one stone.
if occupied_info[-1][1] != 1:
    ans = -1

print(ans)