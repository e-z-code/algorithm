'''
BOJ10259 - Amanda Lounges (https://www.acmicpc.net/problem/10259)

For each edge, you are given how many incident vertices are colored.
Determine the minimum number of colored vertices.
'''

# TIME COMPLEXITY : O(N + M)

import sys
from collections import deque


# 1. TO GET THE INPUT

possible = True

node_count, edge_count = map(int, sys.stdin.readline().split())
lounge = [-1 for node in range(node_count)]

graph = {}
for node in range(node_count):
    graph[node] = []

for edge in range(edge_count):
    nodeA, nodeB, lounge_count = map(int, sys.stdin.readline().split())
    nodeA -= 1
    nodeB -= 1
    # If the value is 0, both vertices must be uncolored.
    if lounge_count == 0:
        if lounge[nodeA] == 1 or lounge[nodeB] == 1:
            possible = False
        lounge[nodeA] = 0
        lounge[nodeB] = 0
    # Only put edges with the value 1 into the graph
    elif lounge_count == 1:
        graph[nodeA].append(nodeB)
        graph[nodeB].append(nodeA)
    # If the value is 2, both vertices must be colored.
    else:
        if lounge[nodeA] == 0 or lounge[nodeB] == 0:
            possible = False
        lounge[nodeA] = 1
        lounge[nodeB] = 1


# 2. TO CHECK IF THE GRAPH IS BIPARTITE - BFS

visited = [0 for node in range(node_count)]

for node in range(node_count):
    if visited[node] == 0:

        queue = deque([(node, node)])
        visited[node] = 1
        
        odd = set()
        even = set([node])
        
        while queue:
            
            now, parent = queue.pop()
            for next in graph[now]:
                if next != parent:
                    if visited[next] == 0:
                        if now in odd:
                            queue.append((next, now))
                            visited[next] = 1
                            even.add(next)
                        else:
                            queue.append((next, now))
                            visited[next] = 1
                            odd.add(next)
                    else:
                        if now in odd:
                            if next in odd:
                                possible = False
                        else:
                            if next in even:
                                possible = False
        
        
        # 3. TO LOCATE THE LOUNGES
        
        odd_zero, odd_one = False, False
        even_zero, even_one = False, False
        
        for node in odd:
            if lounge[node] == 0:
                odd_zero = True
            if lounge[node] == 1:
                odd_one = True
        
        for node in even:
            if lounge[node] == 0:
                even_zero = True
            if lounge[node] == 1:
                even_one = True

        if (odd_zero and odd_one) or (even_zero and even_one) or (odd_zero and even_zero) or (odd_one and even_one):
            possible = False
        
        if odd_one or even_zero:
            for node in odd:
                lounge[node] = 1
            for node in even:
                lounge[node] = 0
        elif odd_zero or even_one:
            for node in odd:
                lounge[node] = 0
            for node in even:
                lounge[node] = 1
        else:
            if len(odd) < len(even):
                for node in odd:
                    lounge[node] = 1
                for node in even:
                    lounge[node] = 0
            else:
                for node in odd:
                    lounge[node] = 0
                for node in even:
                    lounge[node] = 1


# 4. TO GET THE ANSWER

if possible:
    print(sum(lounge))
else:
    print("impossible")
