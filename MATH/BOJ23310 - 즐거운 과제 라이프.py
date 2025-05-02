'''
BOJ23310 - Happy Assignment Life (https://www.acmicpc.net/problem/23310)

There are N assignments.
You do assignment 1 on day 1, assignment 2 on day 2, ..., assignment N on day N, assignment 1 on day N+1, etc.
However, you will take a rest every M days.
Given the number of days to finish each assignment, determine the assignment you can finish first.
'''

# TIME COMPLEXITY : O(NM)

import sys
from math import lcm


# 1. TO GET THE INPUT

homework_count, off_interval = map(int, sys.stdin.readline().split())
to_complete = list(map(int, sys.stdin.readline().split()))


# 2. TO GET THE CYCLE

now_off = off_interval % homework_count

# The order of missed homework in a cycle

off_cycle = []
while len(off_cycle) == 0 or off_cycle[0] != now_off:
    off_cycle.append(now_off)
    now_off = (now_off + off_interval) % homework_count
for idx in range(len(off_cycle)):
    off_cycle[idx] -= 1

cycle_length = lcm(homework_count, off_interval)

# The number of days to do homework in a cycle

on_cycle = [cycle_length // homework_count for count in range(homework_count)]
for homework in off_cycle:
    on_cycle[homework] -= 1


# 3. TO SOLVE THE PROBLEM

# Pass as many cycles as possible

cycle_max = float('inf')

for homework in range(homework_count):
    if on_cycle[homework] == 0:
        continue
    else:
        cycle_max = min(cycle_max, (to_complete[homework] - 1) // on_cycle[homework])

for homework in range(homework_count):
    to_complete[homework] -= on_cycle[homework] * cycle_max

# Last cycle

now_day = 1
now_homework = 0

while True:
    
    if now_day % off_interval == 0:
        now_day += 1
        now_homework = (now_homework + 1) % homework_count
        continue
    
    to_complete[now_homework] -= 1
    if to_complete[now_homework] == 0:
        print(now_homework + 1)
        break
    
    now_day += 1
    now_homework = (now_homework + 1) % homework_count