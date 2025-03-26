'''
BOJ5926 - Cow Lineup (https://www.acmicpc.net/problem/5926)

N cows of different breeds are standing at various positions along a line.
Determine the minimum length of a line with at least one cow of each distinct breed.
'''

# TIME COMPLEXITY : O(N log N)

import sys
from collections import deque
inf = float('inf')


# 3. A FUNCTION FOR SEGMENT TREE

def update(idx, val):
    
    idx += OFFSET
    seg_tree[idx] = [val, val]
    idx >>= 1
    
    while idx != 0:
        seg_tree[idx][0] = min(seg_tree[idx << 1][0], seg_tree[(idx << 1) | 1][0])
        seg_tree[idx][1] = max(seg_tree[idx << 1][1], seg_tree[(idx << 1) | 1][1])
        idx >>= 1


# 1. TO GET THE INPUT

cow_count = int(sys.stdin.readline())

cows = []
breeds = set()

for cow in range(cow_count):
    loc, breed = map(int, sys.stdin.readline().split())
    cows.append((loc, breed))
    breeds.add(breed)

cows.sort()


# 2. COORDINATE COMPRESSION

breed_to_num = {}

now_num = 0
breeds = sorted(list(breeds))
for breed in breeds:
    breed_to_num[breed] = now_num
    now_num += 1


# 4. TO SOLVE THE PROBLEM 
# Consider an array that stores the rightmost x-coordinate for each breed.
# Segment tree stores the minimum and maximum value for each interval.

OFFSET = 1 << 16
node_count = 1 << 17

ans = inf

seg_tree = [[inf, 0] for node in range(node_count)]
now_breeds = set()

for cow in cows:
    loc, breed = cow
    now_breeds.add(breed)
    update(breed_to_num[breed], loc)
    if len(breeds) == len(now_breeds):
        ans = min(ans, seg_tree[1][1] - seg_tree[1][0])

print(ans)