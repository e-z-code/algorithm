'''
BOJ14286 - Organizational Culture 2 (https://www.acmicpc.net/problem/14286)

Given a tree, process the following two queries.

(1) 1 i w : Add w to node i and all descendants.
(2) 2 i : Print the value of node i.
'''

# TIME COMPLEXITY : O(X log X) [X = max(N, M)]

import sys
sys.setrecursionlimit(150000)


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

def get_point(idx):
    
    idx += OFFSET
    
    result = 0
    while idx != 0:
        result += seg_tree[idx]
        idx >>= 1
    
    return result

def update_range(left, right, val):

    left += OFFSET
    right += OFFSET
    
    while left <= right:
        if left % 2 == 1:
            seg_tree[left] += val
            left += 1
        if right % 2 == 0:
            seg_tree[right] += val
            right -= 1
        left >>= 1
        right >>= 1


# 1. TO GET THE INPUT

member_count, query_count = map(int, sys.stdin.readline().split())

parent = list(map(int, sys.stdin.readline().split()))
for member in range(1, member_count):
    parent[member] -= 1

graph = {}
for member in range(member_count):
    graph[member] = []
for member in range(1, member_count):
    graph[parent[member]].append(member)


# 3. ETT

start = [None for node in range(member_count)]
end = [None for node in range(member_count)]

dfs(0)


# 4. TO CONSTRUCT A SEGMENT TREE

OFFSET = 1 << 17
seg_tree = [0 for node in range(1 << 18)]


# 6. TO SOLVE THE PROBLEM

for query in range(query_count):
    
    query_info = list(map(int, sys.stdin.readline().split()))
    
    if query_info[0] == 1:
        member, val = query_info[1], query_info[2]
        member -= 1
        update_range(start[member], end[member], val)
    else:
        member = query_info[1]
        member -= 1
        print(get_point(start[member]))