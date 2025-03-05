'''
BOJ19541 - Epidemiological Survey (https://www.acmicpc.net/problem/19541)

There have been M gatherings.
If a person in a gathering is infected, everyone will be infected.
If not, nothing will happen.
Given infectors after all gatherings, find patient zero(s).
'''

# TIME COMPLEXITY : O(K) [K : Sum of participants of the gathering]

import sys


# 1. TO GET THE INPUT

people_count, group_count = map(int, sys.stdin.readline().split())

groups = []
for group in range(group_count):
    groups.append(list(map(int, sys.stdin.readline().split()[1:])))

goal = [0] + list(map(int, sys.stdin.readline().split()))


# 2. TO GET POSSIBLE INITIAL STATE

state = goal[:]

for idx in range(group_count-1, -1, -1):
    
    group = groups[idx]
    
    no_patient = False
    for person in group:
        if state[person] == 0:
            no_patient = True
            break
    
    if no_patient:
        for person in group:
            state[person] = 0


# 3. SIMULATION

result = state[:]

for idx in range(group_count):
    
    group = groups[idx]
    
    yes_patient = False
    for person in group:
        if result[person] == 1:
            yes_patient = True
            break
    
    if yes_patient:
        for person in group:
            result[person] = 1


# 4. TO SOLVE THE PROBLEM

if result == goal:
    print("YES")
    print(" ".join(map(str, state[1:])))
else:
    print("NO")