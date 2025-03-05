'''
BOJ22273 - Job Allocator (https://www.acmicpc.net/problem/22273)

There are K types of resources.
A machine can share at most R resources, possibly more than one of the same type.
Answer N queries that assign resources to a machine, delete a machine, or ask how many machines satisfy resource requirements.
'''

# TIME COMPLEXITY : O(H(K, R) X pow(2, R))

import sys
from itertools import combinations, combinations_with_replacement


# 1. TO MAP COMBINATIONS
# There are around 13000 cases. Each case has at most 64 subsets.
# Therefore, brute-forcing is possible.

case_num = {}

now_num = 0
for num in range(1, 9):
    for combination in combinations_with_replacement(range(1, 9), num):
        case_num[combination] = now_num
        now_num += 1

graph = {}

for case in case_num.keys():
    graph[case_num[case]] = set()
    for length in range(1, len(case) + 1):
        for combination in combinations(case, length):
            graph[case_num[case]].add(case_num[combination])


# 2. TO GET THE INPUT AND SOLVE THE PROBLEM

query_count, type_count = map(int, sys.stdin.readline().split())

valid_count = [0 for case in range(now_num)]
machines = [-1]

for query in range(query_count):
    
    info = list(sys.stdin.readline().strip().split())
    
    if info[0] == "C":
        
        case = case_num[tuple(sorted(list(map(int, info[2:]))))]
        for valid_case in graph[case]:
            valid_count[valid_case] += 1
        
        machines.append(case)
    
    elif info[0] == "D":
        
        machine = int(info[1])
        case = machines[machine]
        
        for valid_case in graph[case]:
            valid_count[valid_case] -= 1
        
        machines[machine] = -1
    
    else:
        
        case = case_num[tuple(sorted(list(map(int, info[2:]))))]
        print(valid_count[case])