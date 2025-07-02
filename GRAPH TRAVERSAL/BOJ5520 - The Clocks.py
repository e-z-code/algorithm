'''
BOJ5520 - The Clocks (https://www.acmicpc.net/problem/5520)

There are 9 clocks.
There are 9 different allowed ways to turn the dials.
Each way turns the dials 90 degrees clockwise on some clocks.
Return all the dials to 12 o'clock with the fewest moves.
'''

# TIME COMPLEXITY : O(1)

import sys
from collections import deque


# 1. TO GET THE INPUT

clockA, clockB, clockC = map(int, sys.stdin.readline().split())
clockD, clockE, clockF = map(int, sys.stdin.readline().split())
clockG, clockH, clockI = map(int, sys.stdin.readline().split())


# 2. TO SOLVE THE PROBLEM - BFS
# There are at most 4 ^ 9 states.

init_state = (clockA, clockB, clockC, clockD, clockE, clockF, clockG, clockH, clockI)
moves = [(1, 1, 0, 1, 1, 0, 0, 0, 0), (1, 1, 1, 0, 0, 0, 0, 0, 0), (0, 1, 1, 0, 1, 1, 0, 0, 0),
(1, 0, 0, 1, 0, 0, 1, 0, 0), (0, 1, 0, 1, 1, 1, 0, 1, 0), (0, 0, 1, 0, 0, 1, 0, 0, 1),
(0, 0, 0, 1, 1, 0, 1, 1, 0), (0, 0, 0, 0, 0, 0, 1, 1, 1), (0, 0, 0, 0, 1, 1, 0, 1, 1)]

visited = {}

queue = deque([init_state])
visited[init_state] = []

while queue:
    now_state = queue.popleft()
    for idx in range(9):
        
        next_state = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        for clock in range(9):
            next_state[clock] = (now_state[clock] + moves[idx][clock]) % 4
        next_state = tuple(next_state)
        
        if next_state not in visited:
            visited[next_state] = visited[now_state][:]
            visited[next_state].append(str(idx + 1))
            queue.append(next_state)

print(" ".join(visited[(0, 0, 0, 0, 0, 0, 0, 0, 0)]))