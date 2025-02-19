'''
BOJ2962 - Zoo Expansion (https://www.acmicpc.net/problem/2962)

N monkeys pick coconuts at fixed intervals, and M monkeys peel coconuts at fixed intervals.
M monkeys peel coconuts only after N monkeys picked all the coconuts.
Given a time when peeling is finished, determine when picking is completed.
'''

# TIME COMPLEXITY : O(pow(log NT, 2))

import sys


# 1. TO GET THE INPUT

total_time = int(sys.stdin.readline())

get_monkey_count = int(sys.stdin.readline())
get_monkeys = []
for monkey in range(get_monkey_count):
    start, interval = map(int, sys.stdin.readline().split())
    get_monkeys.append((start, interval))

peel_monkey_count = int(sys.stdin.readline())
peel_monkeys = []
for monkey in range(peel_monkey_count):
    start, interval = map(int, sys.stdin.readline().split())
    peel_monkeys.append((start, interval))


# 2. TO SOLVE THE PROBLEM - BINARY SEARCH

ans = None 

# Binary search on the number of coconuts

coconut_left = 0
coconut_right = pow(10, 11) + 1

while coconut_left + 1 < coconut_right:
    
    coconut_count = (coconut_left + coconut_right) // 2
    
    # Binary search on the time needed to get coconuts
    
    get_left = 0
    get_right = coconut_count * pow(10, 9)
    
    while get_left + 1 < get_right:
        
        get_time = (get_left + get_right) // 2
        
        get_count = 0
        for monkey in range(get_monkey_count):
            start, interval = get_monkeys[monkey]
            if get_time >= start:
                get_count += (get_time - start) // interval + 1
        
        if coconut_count <= get_count:
            get_right = get_time
        else:
            get_left = get_time
    
    # Binary search on the time needed to peel coconuts
    
    peel_left = 0
    peel_right = coconut_count * pow(10, 9)
    
    while peel_left + 1 < peel_right:
        
        peel_time = (peel_left + peel_right) // 2
        
        peel_count = 0
        for monkey in range(peel_monkey_count):
            start, interval = peel_monkeys[monkey]
            if peel_time >= start:
                peel_count += (peel_time - start) // interval + 1
        
        if coconut_count <= peel_count:
            peel_right = peel_time
        else:
            peel_left = peel_time
    
    if get_right + peel_right <= total_time:
        coconut_left = coconut_count
        ans = get_right
    else:
        coconut_right = coconut_count

print(ans)
