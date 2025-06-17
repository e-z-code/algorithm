'''
BOJ14571 - Hourglass (https://www.acmicpc.net/problem/14571)

Given a graph, calculate the number of distinct hourglass.
'''

# TIME COMPLEXITY : O(N^3)

import sys


# 1. TO GET THE INPUT

node_count, edge_count = map(int, sys.stdin.readline().split())

graph = [[0 for j in range(node_count)] for i in range(node_count)]

for edge in range(edge_count):
    nodeA, nodeB = map(int, sys.stdin.readline().split())
    nodeA -= 1
    nodeB -= 1
    graph[nodeA][nodeB] = 1
    graph[nodeB][nodeA] = 1


# 2. TO COUNT THE NUMBER OF TRIANGLES

triangle_containing_point = {}
for node in range(node_count):
    triangle_containing_point[node] = 0
    
triangle_containing_line = {}
for nodeA in range(node_count):
    for nodeB in range(node_count):
        triangle_containing_line[(nodeA, nodeB)] = 0

for nodeA in range(node_count):
    for nodeB in range(nodeA + 1, node_count):
        for nodeC in range(nodeB + 1, node_count):
            
            if graph[nodeA][nodeB] and graph[nodeB][nodeC] and graph[nodeA][nodeC]:
                
                triangle_containing_point[nodeA] += 1
                triangle_containing_point[nodeB] += 1
                triangle_containing_point[nodeC] += 1
                
                triangle_containing_line[(nodeA, nodeB)] += 1
                triangle_containing_line[(nodeA, nodeC)] += 1
                triangle_containing_line[(nodeB, nodeC)] += 1


# 3. TO SOLVE THE PROBLEM

ans = 0

for center_node in range(node_count):
    # Choose two triangles that both contains a center node
    hourglass_count = triangle_containing_point[center_node] * (triangle_containing_point[center_node] - 1) // 2
    # Subtract cases when two triangles share a line
    for node in range(node_count):
        if center_node < node:
            hourglass_count -= triangle_containing_line[(center_node, node)] * (triangle_containing_line[(center_node, node)] - 1) // 2
        elif center_node > node:
            hourglass_count -= triangle_containing_line[(node, center_node)] * (triangle_containing_line[(node, center_node)] - 1) // 2
    ans += hourglass_count

print(ans)