'''
BOJ10999 - Range Sum 2 (https://www.acmicpc.net/problem/10999)

There is an array A of N integers.
Process the following two queries.

(1) 1 i j k : Add k to A[i], ..., A[j].
(2) 2 i j : Print A[i] + ... + A[j].
'''

# TIME COMPLEXITY : O(max(M, K) log max(M, K))

import sys


# 2. FUNCTIONS FOR SEGMENT TREE WITH LAZY PROPAGATION

# Lazy propagation

def propagate_lazy(node, seg_left, seg_right):

    if lazy[node] != 0:
        seg_tree[node] += (seg_right - seg_left + 1) * lazy[node]
        if seg_left != seg_right:
            lazy[node << 1] += lazy[node]
            lazy[(node << 1) | 1] += lazy[node]
        lazy[node] = 0

    return

# To update range

def update_range(node, range_left, range_right, seg_left, seg_right, val):

    propagate_lazy(node, seg_left, seg_right)
    
    # Not included
    if range_right < seg_left or seg_right < range_left:
        return
    
    # Included
    if range_left <= seg_left and seg_right <= range_right:
        lazy[node] += val
        propagate_lazy(node, seg_left, seg_right)
        return 
    
    # Overlapped
    update_range(node << 1, range_left, range_right, seg_left, (seg_left + seg_right) // 2, val)
    update_range((node << 1) | 1, range_left, range_right, (seg_left + seg_right) // 2 + 1, seg_right, val)
    seg_tree[node] = seg_tree[node << 1] + seg_tree[(node << 1) | 1]

# To get sum of range

def range_sum(node, range_left, range_right, seg_left, seg_right):
    
    propagate_lazy(node, seg_left, seg_right)
    
    # Not Included
    if range_right < seg_left or seg_right < range_left:
        return 0
    
    # Included
    if range_left <= seg_left and seg_right <= range_right:
        return seg_tree[node]

    # Overlapped
    left_sum = range_sum(node << 1, range_left, range_right, seg_left, (seg_left + seg_right) // 2)
    right_sum = range_sum((node << 1) | 1, range_left, range_right, (seg_left + seg_right) // 2 + 1, seg_right)
    return left_sum + right_sum


# 1. TO GET THE INPUT AND CONSTRUCT A SEGMENT TREE

num_count, update_count, sum_count = map(int, sys.stdin.readline().split())

# Segment tree

OFFSET = 1 << 20
node_count = 1 << 21

seg_tree = [0 for node in range(node_count)]
lazy = [0 for node in range(node_count)]

for idx in range(num_count):
    node = idx + OFFSET
    seg_tree[node] = int(sys.stdin.readline())

for idx in range(OFFSET-1, 0, -1):
    seg_tree[idx] = seg_tree[idx << 1] + seg_tree[(idx << 1) | 1]


# 3. TO SOLVE THE PROBLEM

for query in range(update_count + sum_count):
    
    query_info = list(map(int, sys.stdin.readline().split()))
    
    if query_info[0] == 1:
        left, right, val = query_info[1], query_info[2], query_info[3]
        left -= 1
        right -= 1
        update_range(1, left, right, 0, OFFSET-1, val)
    else:
        left, right = query_info[1], query_info[2]
        left -= 1
        right -= 1
        print(range_sum(1, left, right, 0, OFFSET-1))