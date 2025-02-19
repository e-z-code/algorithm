'''
BOJ9887 - Genome (https://www.acmicpc.net/problem/9887)

Given M strings, determine the length of the longest string, which is the subsequence of all M strings.
'''

# TIME COMPLEXITY : O(MN^2)

import sys
from collections import deque


# 1. TO GET THE INPUT

num_count, species_count = map(int, sys.stdin.readline().split())

graph = [[0 for numB in range(num_count + 1)] for numA in range(num_count + 1)]

for species in range(species_count):
    
    gene = list(map(int, sys.stdin.readline().split()))
    
    for i in range(num_count):
        for j in range(i+1, num_count):
            graph[gene[i]][gene[j]] += 1


# 2. TO CONSTRUCT DAG

t_graph = {}
in_degree = {}

for num in range(1, num_count + 1):
    t_graph[num] = []
    in_degree[num] = 0

for numA in range(1, num_count + 1):
    for numB in range(1, num_count + 1):
        if graph[numA][numB] == species_count:
            t_graph[numA].append(numB)
            in_degree[numB] += 1


# 3. TOPOLOGICAL SORT

t_sort = deque([])
ans = [0 for num in range(num_count + 1)]

for num in range(1, num_count + 1):
    if in_degree[num] == 0:
        ans[num] = 1
        t_sort.append(num)

while t_sort:
    now_num = t_sort.popleft()
    for next_num in t_graph[now_num]:
        in_degree[next_num] -= 1
        ans[next_num] = max(ans[next_num], ans[now_num] + 1)
        if in_degree[next_num] == 0:
            t_sort.append(next_num)

print(max(ans))