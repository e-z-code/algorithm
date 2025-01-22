'''
BOJ9001 - Rectangle Coloring (https://www.acmicpc.net/problem/9001)

You want to color N rectangles.
If two rectangles are overlapped, they should have the same color.
If not, they should have different colors.
Determine the minimum number of colors needed.
'''

# TIME COMPLEXITY : O(N^2)

import sys
from collections import deque


# 2. A FUNCTION TO CHECK INTERSECTION

def intersection(rectangleA, rectangleB):
    
    x1, y1, x2, y2 = rectangleA
    x3, y3, x4, y4 = rectangleB
    
    if x4 < x1 or x2 < x3 or y4 < y1 or y2 < y3:
        return False
    else:
        return True


# 1. TO GET THE INPUT

test_count = int(sys.stdin.readline())

for test in range(test_count):
    
    rectangle_count = int(sys.stdin.readline())
    
    rectangles = []
    for rectangle in range(rectangle_count):
        x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
        rectangles.append((x1, y1, x2, y2))
    
    
    # 3. TO CONSTRUCT THE GRAPH
    
    graph = {}
    for idx in range(rectangle_count):
        graph[idx] = []
    
    for i in range(rectangle_count):
        for j in range(i+1, rectangle_count):
            if intersection(rectangles[i], rectangles[j]):
                graph[i].append(j)
                graph[j].append(i)
    
    
    # 4. TO SOLVE THE PROBLEM - BFS
    
    ans = 0
    visited = [0 for idx in range(rectangle_count)]
    
    for idx in range(rectangle_count):
        if visited[idx] == 0:
            
            queue = deque([idx])
            visited[idx] = 1
            
            while queue:
                now_node = queue.popleft()
                for next_node in graph[now_node]:
                    if visited[next_node] == 0:
                        queue.append(next_node)
                        visited[next_node] = 1
            
            ans += 1
    
    print(ans)