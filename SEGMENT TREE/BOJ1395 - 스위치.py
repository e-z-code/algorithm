'''
BOJ1395 - Switch (https://www.acmicpc.net/problem/1395)

There are N switches from number 1 to N.
Process the following two queries.

(1) Reverse the state of switches from numbers A to B.
(2) Count the switches turned on from numbers C to D.
'''

# TIME COMPLEXITY : O(X log X) [X = max(N, M)]

import sys


# 2. FUNCTIONS FOR SEGMENT TREE WITH LAZY PROPAGATION

# Lazy propagation

def propagate_lazy(node, seg_left, seg_right):

    if lazy[node] != 0:
        
        if lazy[node] % 2 == 1:
            seg_tree[node] = (seg_right - seg_left + 1) - seg_tree[node]
        
        if seg_left != seg_right:
            lazy[node << 1] += lazy[node]
            lazy[(node << 1) | 1] += lazy[node]
        
        lazy[node] = 0

    return

# To update range

def update_range(node, range_left, range_right, seg_left, seg_right):

    propagate_lazy(node, seg_left, seg_right)
    
    # Not included
    if range_right < seg_left or seg_right < range_left:
        return
    
    # Included
    if range_left <= seg_left and seg_right <= range_right:
        lazy[node] += 1
        propagate_lazy(node, seg_left, seg_right)
        return 
    
    # Overlapped
    update_range(node << 1, range_left, range_right, seg_left, (seg_left + seg_right) // 2)
    update_range((node << 1) | 1, range_left, range_right, (seg_left + seg_right) // 2 + 1, seg_right)
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


# 1. TO GET THE INPUT AND CONSTRUCT SEGMENT TREE

switch_count, query_count = map(int, sys.stdin.readline().split())

# Segment tree

OFFSET = 1 << 17
node_count = 1 << 18

seg_tree = [0 for node in range(node_count)]
lazy = [0 for node in range(node_count)]


# 3. TO SOLVE THE PROBLEM

for query in range(query_count):
    
    query_num, left, right = map(int, sys.stdin.readline().split())
    left -= 1
    right -= 1
    
    if query_num == 0:
        update_range(1, left, right, 0, OFFSET-1)
    else:
        print(range_sum(1, left, right, 0, OFFSET-1))