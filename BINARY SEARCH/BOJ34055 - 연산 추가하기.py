'''
BOJ34055 - Operation Addition (https://www.acmicpc.net/problem/34055)

There are N lines on a horizontal line of length H.

Answer Q queries:
You want to draw a new line of length T.
How many starting points are there such that the new line does not intersect the other lines?
'''

# TIME COMPLEXITY : O((N + Q) log N)

import sys


# 1. TO GET THE INPUT

line_count, max_length = map(int, sys.stdin.readline().split())

lines = []
for line in range(line_count):
    start, end = map(int, sys.stdin.readline().split())
    lines.append((start, end))
lines.sort()


# 2. UNION ALL LINES

lines_union = []

now_start = None
now_end = None
for idx in range(line_count):
    start, end = lines[idx]
    if idx == 0:
        now_start = start
        now_end = end
    else:
        if start <= now_end:
            now_end = max(end, now_end)
        else:
            lines_union.append((now_start, now_end))
            now_start = start
            now_end = end

if now_start != None and now_end != None:
    lines_union.append((now_start, now_end))


# 3. TO STORE LENGTH OF EMPTY LINES

empty_length = []

empty_start = 1
for start, end in lines_union:
    if empty_start < start:
        empty_length.append(start - empty_start)
    empty_start = end + 1
if empty_start <= max_length:
    empty_length.append(max_length - empty_start + 1)

empty_length.sort(reverse=True)


# 4. PREFIX SUM

prefix_sum = []

for idx in range(len(empty_length)):
    if idx == 0:
        prefix_sum.append(empty_length[idx])
    else:
        prefix_sum.append(empty_length[idx] + prefix_sum[-1])


# 5. TO SOLVE THE PROBLEM - BINARY SEARCH

query_count = int(sys.stdin.readline())

for query in range(query_count):
    
    new_length = int(sys.stdin.readline())
    
    if len(empty_length) == 0:
        print(0)
    else:
        if new_length > empty_length[0]:
            print(0)
        else:
            
            left = 0
            right = len(empty_length) - 1
            while left + 1 < right:
                mid = (left + right) // 2
                if new_length <= empty_length[mid]:
                    left = mid
                else:
                    right = mid
            
            if new_length <= empty_length[right]:
                key_idx = right
            else:
                key_idx = left
                
            print(prefix_sum[key_idx] - (key_idx + 1) * (new_length - 1))