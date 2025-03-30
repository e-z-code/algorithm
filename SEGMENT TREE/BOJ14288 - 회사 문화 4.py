'''
BOJ14288 - Organizational Culture 4 (https://www.acmicpc.net/problem/14288)

Given a tree, process the following three queries.

(1) 1 i w : Add w to node i. If a direction is upward, add w to all ancestors. Otherwise, add w to all descendants.
(2) 2 i : Print the value of node i.
(3) 3 : Change the direction.
'''

# TIME COMPLEXITY : O(X log X) [X = max(N, M)]

import sys


# 2. DFS FUNCTION FOR ETT (EULER TOUR TECHNIQUE)

now_num = 0

def dfs(now_node):
    
    global now_num
    
    start[now_node] = now_num
    now_num += 1
    for next_node in graph[now_node]:
        dfs(next_node)
    end[now_node] = now_num - 1


# 5. FUNCTIONS FOR SEGMENT TREE

def point_update(idx, val):
    
    idx += OFFSET
    
    while idx != 0:
        up_seg_tree[idx] += val
        idx >>= 1

def range_sum(left, right):
    
    left += OFFSET
    right += OFFSET
    
    result = 0
    while left <= right:
        if left % 2 == 1:
            result += up_seg_tree[left]
            left += 1
        if right % 2 == 0:
            result += up_seg_tree[right]
            right -= 1
        left >>= 1
        right >>= 1
    
    return result

def range_update(left, right, val):
    
    left += OFFSET
    right += OFFSET
    
    while left <= right:
        if left % 2 == 1:
            down_seg_tree[left] += val 
            left += 1
        if right % 2 == 0:
            down_seg_tree[right] += val
            right -= 1
        left >>= 1
        right >>= 1
    
def point_sum(idx):
    
    idx += OFFSET
    
    result = 0
    while idx != 0:
        result += down_seg_tree[idx]
        idx >>= 1
        
    return result


# 1. TO GET THE INPUT

member_count, query_count = map(int, sys.stdin.readline().split())
parent = list(map(int, sys.stdin.readline().split()))

graph = {}
for member in range(member_count):
    graph[member] = []
for member in range(1, member_count):
    graph[parent[member] - 1].append(member)


# 3. ETT

start = [-1 for idx in range(member_count)]
end = [-1 for idx in range(member_count)]

dfs(0)


# 4. TO CONSTRUCT SEGMENT TREES

node_count = 1 << 18
OFFSET = 1 << 17

up_seg_tree = [0 for node in range(node_count)]
down_seg_tree = [0 for node in range(node_count)]


# 6. TO SOLVE THE PROBLEM

upward = False

for query in range(query_count):
    
    query_info = list(map(int, sys.stdin.readline().split()))
    
    if query_info[0] == 1:
        member, val = query_info[1], query_info[2]
        member -= 1
        if upward:
            point_update(start[member], val)
        else:
            range_update(start[member], end[member], val)
    elif query_info[0] == 2:
        member = query_info[1]
        member -= 1
        print(range_sum(start[member], end[member]) + point_sum(start[member]))
    else:
        upward = not upward