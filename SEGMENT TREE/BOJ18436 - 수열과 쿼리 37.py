'''
BOJ18436 - Sequence and Queries 37 (https://www.acmicpc.net/problem/18436)

Given a sequence A, process the three following types of queries.

(1) Change A[i] to v.
(2) Print the number of even numbers in A[i:j+1].
(3) Print the number of odd numbers in A[i:j+1].
'''

# TIME COMPLEXITY : O(X log X) [X = max(N, M)]

import sys


# 3. FUNCTIONS FOR SEGMENT TREE

def update(idx, val):
    
    node = idx + OFFSET
    seg_tree[node] = val
    node >>= 1
    
    while node != 0:
        seg_tree[node] = seg_tree[node << 1] + seg_tree[(node << 1) | 1]
        node >>= 1

def even_count(left, right):
    
    left += OFFSET
    right += OFFSET
    
    result = 0
    
    while left <= right:
        if left % 2 == 1:
            result += seg_tree[left]
            left += 1
        if right % 2 == 0:
            result += seg_tree[right]
            right -= 1
        left >>= 1
        right >>= 1
    
    return result


# 1. TO GET THE INPUT

length = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))


# 2. TO CONSTRUCT A SEGMENT TREE
# The segment tree stores a number of even numbers.

OFFSET = 1 << 17
node_count = 1 << 18

seg_tree = [0 for node in range(node_count)]

for idx in range(length):
    if arr[idx] % 2 == 0:
        node = idx + OFFSET
        seg_tree[node] += 1

for node in range(OFFSET-1, 0, -1):
    seg_tree[node] = seg_tree[node << 1] + seg_tree[(node << 1) | 1]


# 4. TO SOLVE THE PROBLEM

query_count = int(sys.stdin.readline())

for query in range(query_count):
    
    query_info = list(map(int, sys.stdin.readline().split()))
    
    if query_info[0] == 1:
        idx, val = query_info[1], query_info[2]
        idx -= 1
        if val % 2 == 0:
            update(idx, 1)
        else:
            update(idx, 0)
    elif query_info[0] == 2:
        left, right = query_info[1], query_info[2]
        left -= 1
        right -= 1
        print(even_count(left, right))
    else:
        left, right = query_info[1], query_info[2]
        left -= 1
        right -= 1
        print(right - left + 1 - even_count(left, right))