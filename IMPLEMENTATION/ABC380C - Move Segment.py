'''
ABC380C - Move Segment (https://atcoder.jp/contests/abc380/tasks/abc380_c)

There is a binary string of length N.
Move the K-th 1-block from the beginning to immediately after the (K-1)-th 1-block.
'''

# TIME COMPLEXITY : O(N)

import sys


# 1. TO GET THE INPUT

length, target = map(int, sys.stdin.readline().split())
target -= 1
string = sys.stdin.readline().strip()


# 2. RECORD 1-BLOCKS

one_blocks = []

start = None
end = None

for idx in range(length):
    
    char = string[idx]
    
    if char == "0":
        if start != None:
            one_blocks.append((start, end))
            start = None
            end = None
    else:
        if start == None:
            start = idx
            end = idx
        else:
            end = idx

if start != None:
    one_blocks.append((start, end))


# 3. TO SOLVE THE PROBLEM

block_length = one_blocks[target][1] - one_blocks[target][0] + 1
one_blocks[target] = (one_blocks[target-1][1] + 1, one_blocks[target-1][1] + block_length)

ans = ["0" for idx in range(length)]

for start, end in one_blocks:
    for idx in range(start, end+1):
        ans[idx] = "1"

print("".join(ans))