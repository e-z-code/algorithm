'''
BOJ23740 - Bus Line Reorganization (https://www.acmicpc.net/problem/23740)

There are N weighted segments.
Two segments can be combined if they overlap, and the weight of the combined segment would be the minimum one.
Print the result after combing all possible segments.
'''

# TIME COMPLEXITY : O(N log N)

import sys


# 1. TO GET THE INPUT

line_count = int(sys.stdin.readline())

lines = []
for line in range(line_count):
    start, end, cost = map(int, sys.stdin.readline().split())
    lines.append((start, end, cost))
lines.sort()


# 2. TO COMBINE LINES

new_lines = []

now_start, now_end, now_cost = lines[0]

for idx in range(1, line_count):
    
    start, end, cost = lines[idx]
    
    if now_end >= start:
        now_end = max(now_end, end)
        now_cost = min(now_cost, cost)
    else:
        new_lines.append((now_start, now_end, now_cost))
        now_start, now_end, now_cost = start, end, cost

new_lines.append((now_start, now_end, now_cost))


# 3. TO SOLVE THE PROBLEM

print(len(new_lines))
for line in new_lines:
    start, end, cost = line
    print(start, end, cost)