'''
BOJ18437 - Organizational Culture 5 (https://www.acmicpc.net/problem/18437)

Given a tree, process the following three queries.
Initially, all computers are on.

(1) 1 i : Every descendant of i turns on a computer.
(2) 2 i : Every descendant of i turns off a computer.
(3) 3 i : Print the number of descendants of i whose computer is on.
'''

# TIME COMPLEXITY : O(X log X) [X = max(N, M)]


import sys
sys.setrecursionlimit(100050)


# 2. A FUNCTION FOR ETT (EULER TOUR TECHNIQUE)

now_num = 0

def dfs(now_node):
    
    global now_num
    
    now_num += 1
    start[now_node] = now_num
    
    for next_node in graph[now_node]:
        dfs(next_node)    
    end[now_node] = now_num - 1


# 4. FUNCTIONS FOR SEGMENT TREE WITH LAZY PROPAGATION

def propagate_lazy(node, seg_left, seg_right):
    
    if lazy[node] != -1:
        
        if lazy[node] % 2 == 0:
            seg_tree[node] = 0
        else:
            seg_tree[node] = seg_right - seg_left + 1
        
        if seg_left != seg_right:
            lazy[node << 1] = lazy[node]
            lazy[(node << 1) | 1] = lazy[node]

        lazy[node] = -1
    
    return

def range_update(node, range_left, range_right, seg_left, seg_right, val):
    
    propagate_lazy(node, seg_left, seg_right)
    
    if range_right < seg_left or seg_right < range_left:
        return

    if range_left <= seg_left and seg_right <= range_right:
        lazy[node] = val
        propagate_lazy(node, seg_left, seg_right)
        return

    range_update(node << 1, range_left, range_right, seg_left, (seg_left + seg_right) // 2, val)
    range_update((node << 1) | 1, range_left, range_right, (seg_left + seg_right) // 2 + 1, seg_right, val)
    seg_tree[node] = seg_tree[node << 1] + seg_tree[(node << 1) | 1]

def range_sum(node, range_left, range_right, seg_left, seg_right):
    
    propagate_lazy(node, seg_left, seg_right)
    
    if range_right < seg_left or seg_right < range_left:
        return 0
    
    if range_left <= seg_left and seg_right <= range_right:
        return seg_tree[node]
    
    left_sum = range_sum(node << 1, range_left, range_right, seg_left, (seg_left + seg_right) // 2)
    right_sum = range_sum((node << 1) | 1, range_left, range_right, (seg_left + seg_right) // 2 + 1, seg_right)
    return left_sum + right_sum


# 1. TO GET THE INPUT

member_count = int(sys.stdin.readline())

parent = list(map(int, sys.stdin.readline().split()))

graph = {}
for member in range(member_count):
    graph[member] = []
for member in range(member_count):
    if parent[member] != 0:
        graph[parent[member] - 1].append(member)


# 3. ETT

start = [-1 for member in range(member_count)]
end = [-1 for member in range(member_count)]

dfs(0)


# 5. TO CONSTRUCT SEGMENT TREE

node_count = 1 << 18
OFFSET = 1 << 17

lazy = [-1 for node in range(node_count)]
seg_tree = [0 for node in range(node_count)]

for idx in range(member_count):
    idx += OFFSET
    seg_tree[idx] = 1

for node in range(OFFSET-1, 0, -1):
    seg_tree[node] = seg_tree[node << 1] + seg_tree[(node << 1) | 1]


# 6. TO SOLVE THE PROBLEM

query_count = int(sys.stdin.readline())

for query in range(query_count):
    
    query_type, member = list(map(int, sys.stdin.readline().split()))
    member -= 1
    
    if query_type == 1:
        range_update(1, start[member], end[member], 0, OFFSET-1, 1)
    elif query_type == 2:
        range_update(1, start[member], end[member], 0, OFFSET-1, 0)
    else:
        print(range_sum(1, start[member], end[member], 0, OFFSET-1))