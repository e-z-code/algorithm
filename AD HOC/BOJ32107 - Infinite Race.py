'''
BOJ32107 - Infinite Race (https://www.acmicpc.net/problem/32107)

You participate in an infinite marathon on a running track.
You know when you overtook someone or when someone overtook you.
Given records, determine the minimum possible laps you are in.
'''

# TIME COMPLEXITY : O(max(N, M))

import sys


# 1. TO GET THE INPUT

runner_count = int(sys.stdin.readline())
event_count = int(sys.stdin.readline())


# 2. TO SOLVE THE PROBLEM
# What only matters is when you overtakes someone behind you. 

ans = 0

front = [1 for runner in range(runner_count)]
takeover = set()

for event_num in range(event_count):
    
    event = int(sys.stdin.readline())
    
    if event < 0:
        runner = -event
        front[runner] = 1
    else:
        runner = event
        if front[runner]:
            front[runner] = 0
            takeover.add(runner)
        else:
            if len(takeover) == 0 or runner in takeover:
                ans += 1
                takeover = set([runner])
            else:
                takeover.add(runner)

print(ans)