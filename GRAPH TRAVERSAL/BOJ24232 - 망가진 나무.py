'''
BOJ24232 - Corrupt Tree (https://www.acmicpc.net/problem/24232)

There is a tree.
However, each edge transformed into a directional edge.
You can reverse the direction of each edge.
Your goal is to construct a graph so that there is a node that can reach every other node.
Determine which edges to reverse.
'''

# TIME COMPLEXITY : O(N)

import sys
from collections import deque
sys.setrecursionlimit(200000)


# 3. DFS FUNCTION TO FIND THE START NODE
# The only edge to reverse is an edge between the current node and its child node.

def dfs(now_node, parent_node):
    
    global reverse_count, ans_node, ans_count
    
    for next_node in graph[now_node]:
        if next_node != parent_node:
            
            if (now_node, next_node) in edge_to_num:
                edge_num = edge_to_num[(now_node, next_node)]
            else:
                edge_num = edge_to_num[(next_node, now_node)]
                
            if reverse_state[edge_num] == 0:
                reverse_state[edge_num] = 1
                reverse_count += 1
            else:
                reverse_state[edge_num] = 0
                reverse_count -= 1
            
            if reverse_count < ans_count:
                ans_node = next_node
                ans_count = reverse_count
            
            dfs(next_node, now_node)
            
            if reverse_state[edge_num] == 0:
                reverse_state[edge_num] = 1
                reverse_count += 1
            else:
                reverse_state[edge_num] = 0
                reverse_count -= 1


# 1. TO GET THE INPUT

node_count = int(sys.stdin.readline())

graph = {}
for node in range(node_count):
    graph[node] = []

edge_to_num = {}
for edge in range(node_count - 1):
    nodeA, nodeB = map(int, sys.stdin.readline().split())
    nodeA -= 1
    nodeB -= 1
    edge_to_num[(nodeA, nodeB)] = edge
    graph[nodeA].append(nodeB)
    graph[nodeB].append(nodeA)


# 2. BFS TO ALGIN EDGES FROM NODE 0

reverse_state = [0 for edge in range(node_count - 1)]

visited = [0 for idx in range(node_count)]

queue = deque([0])
visited[0] = 1

while queue:
    now_node = queue.popleft()
    for next_node in graph[now_node]:
        if visited[next_node] == 0:
            queue.append(next_node)
            visited[next_node] = 1
            if (now_node, next_node) not in edge_to_num:
                reverse_state[edge_to_num[(next_node, now_node)]] += 1

reverse_count = reverse_state.count(1)


# 4. BFS TO GET THE ANSWER STATE

ans_node = 0
ans_count = reverse_count

dfs(0, -1)

ans_state = [0 for edge in range(node_count - 1)]

visited = [0 for idx in range(node_count)]

queue = deque([ans_node])
visited[ans_node] = 1

while queue:
    now_node = queue.popleft()
    for next_node in graph[now_node]:
        if visited[next_node] == 0:
            queue.append(next_node)
            visited[next_node] = 1
            if (now_node, next_node) not in edge_to_num:
                ans_state[edge_to_num[(next_node, now_node)]] += 1

print("".join(map(str, ans_state)))