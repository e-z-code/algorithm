'''
BOJ14245 - XOR (https://www.acmicpc.net/problem/14245)

Given an array A, process the following two queries.

(1) 1 a b c : Change A[i] to A[i] XOR c for all a <= i <= b.
(2) 2 a : Print A[a].
'''

# TIME COMPLEXITY : O(N log N)

import sys


# 3. FUNCTIONS FOR SEGMENT TREE

def range_xor(left, right, val):
    
    left += OFFSET
    right += OFFSET
    
    while left <= right:
        if left % 2 == 1:
            seg_tree[left] ^= val
            left += 1
        if right % 2 == 0:
            seg_tree[right] ^= val
            right -= 1
        left >>= 1
        right >>= 1

def get_val(idx):
    
    node = idx + OFFSET
    
    result = 0
    while node != 0:
        result ^= seg_tree[node]
        node >>= 1
    
    return result


# 1. TO GET THE INPUT

length = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))


# 2. TO CONSTRUCT A SEGMENT TREE

node_count = 1 << 20
OFFSET = 1 << 19

seg_tree = [0 for node in range(node_count)]
for idx in range(length):
    seg_tree[idx + OFFSET] = arr[idx]


# 4. TO SOLVE THE PROBLEM

query_count = int(sys.stdin.readline())

for query in range(query_count):
    
    query_info = list(map(int, sys.stdin.readline().split()))
    
    if query_info[0] == 1:
        idxA, idxB, val = query_info[1:]
        range_xor(idxA, idxB, val)
    else:
        idx = query_info[1]
        print(get_val(idx))