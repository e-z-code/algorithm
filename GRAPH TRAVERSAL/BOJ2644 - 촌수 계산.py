'''
BOJ2644 - Degree of Kinship (https://www.acmicpc.net/problem/2644)

Given a family relationship, determine the degree of kinship between two family members.
'''

# TIME COMPLEXITY : O(N+M)


import sys
from collections import deque


# 1. TO GET THE INPUT

member_count = int(sys.stdin.readline())
start, end = map(int, sys.stdin.readline().split())
start -= 1
end -= 1

graph = {}
for member in range(member_count):
    graph[member] = []

relation_count = int(sys.stdin.readline())
for relation in range(relation_count):
    memberA, memberB = map(int, sys.stdin.readline().split())
    graph[memberA-1].append(memberB-1)
    graph[memberB-1].append(memberA-1)


# 2. TO SOLVE THE PROBLEM - BFS
# Degree of kinship equals the minimum distance over given relationship network.

visited = [-1 for member in range(member_count)]

queue = deque([start])
visited[start] = 0

while queue:
    now_member = queue.popleft()
    for next_member in graph[now_member]:
        if visited[next_member] == -1:
            visited[next_member] = visited[now_member] + 1
            queue.append(next_member)

print(visited[end])