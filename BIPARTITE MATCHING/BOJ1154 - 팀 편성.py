'''
BOJ1154 - Team Matching (https://www.acmicpc.net/problem/1154)

You want to divide N students into two teams.
Each student should be on either team A or team B, and students on the same team must know each other.
Determine if it is possible to divide students into two teams.
If possible, make two teams.
'''

# TIME COMPLEXITY : O(N^2)

import sys
from collections import deque


# 1. TO GET THE INPUT AND CONSTRUCT GRAPH
# Connect two students if they do not know each other.

student_count = int(sys.stdin.readline())

graph = [[1 for j in range(student_count)] for i in range(student_count)]

for student in range(student_count):
    graph[student][student] = 0

while True:
    
    studentA, studentB = map(int, sys.stdin.readline().split())
    if studentA == -1 and studentB == -1:
        break
    
    studentA -= 1
    studentB -= 1
    
    graph[studentA][studentB] = 0
    graph[studentB][studentA] = 0


# 2. TO CHECK IF THE GRAPH IS BIPARTITE GRAPH

is_bipartite = True

visited = [-1 for student in range(student_count)]

for student in range(student_count):
    if is_bipartite and visited[student] == -1:
        
        queue = deque([student])
        visited[student] = 0
        
        while queue:
            now_student = queue.popleft()
            for next_student in range(student_count):
                if graph[now_student][next_student]:
                    if visited[next_student] == -1:
                        queue.append(next_student)
                        visited[next_student] = visited[now_student] + 1
                    else:
                        if visited[now_student] % 2 == visited[next_student] % 2:
                            is_bipartite = False


# 3. TO SOLVE THE PROBLEM

if is_bipartite:
    
    print(1)
    
    teamA = []
    teamB = []
    
    for student in range(student_count):
        if visited[0] % 2 == visited[student] % 2:
            teamA.append(student + 1)
        else:
            teamB.append(student + 1)
    
    teamA.append(-1)
    teamB.append(-1)
    
    print(" ".join(map(str, teamA)))
    print(" " .join(map(str, teamB)))
    
else:
    
    print(-1)