'''
BOJ23578 - Rainy Day (https://www.acmicpc.net/problem/23578)

There are N weighted nodes.
If the degree of a node of weight W is K, the cost of the node is W * pow(K, 2).
Construct a graph such that all N nodes are connected and the cost sum is minimal.
'''

# TIME COMPLEXITY : O(N log N)

import sys, heapq


# 1. TO GET THE INPUT

building_count = int(sys.stdin.readline())
students_count = list(map(int, sys.stdin.readline().split()))
students_count.sort()


# 2. TO CONNECT NODES
# Connect from nodes with the smallest weight.
# Connect to a node that minimizes the increase of cost sum.

heap = []

for student_count in students_count:
    
    if len(heap) == 0:
        heapq.heappush(heap, (student_count, student_count, 0))
    else:
        # If a new node is connected to a node of weight W that has a degree of K, increase would be (2W + 1)K.
        delta, weight, degree = heapq.heappop(heap)
        heapq.heappush(heap, ((2 * (degree + 1) + 1) * weight, weight, degree + 1))
        heapq.heappush(heap, (3 * student_count, student_count, 1))


# 3. TO SOLVE THE PROBLEM

ans = 0

while heap:
    
    delta, weight, degree = heapq.heappop(heap)
    ans += pow(degree, 2) * weight

print(ans) 