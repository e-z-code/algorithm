'''
BOJ24563 - Pinned Files (https://www.acmicpc.net/problem/24563)

There is a list of files.
If a pinned file is unpinned, it is removed from the lst and added before the first unpinned file.
If an unpinned file is pinned, it is removed and then added after the last pinned file.
Given the initial state of files, determine the minimum number of moves to reach the goal status.
'''

# TIME COMPLEXITY : O(N^2)

import sys


# 1. TO GET THE INPUT

start_pinned_count, start_unpinned_count = map(int, sys.stdin.readline().split())
start_state = list(map(int, sys.stdin.readline().split()))
start_pinned = start_state[:start_pinned_count]
start_unpinned = start_state[start_pinned_count:]

end_pinned_count, end_unpinned_count = map(int, sys.stdin.readline().split())
end_state = list(map(int, sys.stdin.readline().split()))
end_pinned = end_state[:end_pinned_count]
end_unpinned = end_state[end_pinned_count:]


# 2. TO SOLVE THE PROBLEM

# The list stores the minimal move needed to put a file in the right order. 
# It is initialized to 1 for the case when there is no pinned (or unpinned) file at the beginning. 

move = [1 for idx in range(start_pinned_count + start_unpinned_count)] 

# Pinned files

i = 0
j = 0

while i < start_pinned_count and j < end_pinned_count:
    if start_state[i] == end_state[j]:
        move[i] = 0
        i += 1
        j += 1
    else:
        if start_state[i] not in end_pinned:
            move[i] = 1
        else:
            move[i] = 2
        i += 1

# Unpinned files

i = 1
j = 1

while i <= start_unpinned_count and j <= end_unpinned_count:
    if start_state[-i] == end_state[-j]:
        move[-i] = 0
        i += 1
        j += 1
    else:
        if start_state[-i] not in end_unpinned:
            move[-i] = 1
        else:
            move[-i] = 2
        i += 1

print(sum(move))