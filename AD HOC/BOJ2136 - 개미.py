'''
BOJ2136 - Ants (https://www.acmicpc.net/problem/2136)

There are N ants on a horizontal line of length L.
Each ant moves either left or right at the speed of 1.
If two ants collide, both ants change direction, but their speeds do not change.
Determine the ant that falls last and the time it falls.
'''

# TIME COMPLEXITY : O(N log N)

import sys


# 1. TO GET THE INPUT

ant_count, length = map(int, sys.stdin.readline().split())

ants = []
for ant in range(1, ant_count + 1):
    loc = int(sys.stdin.readline())
    if loc > 0:
        ants.append((loc, 0, ant))
    else:
        ants.append((-loc, 1, ant))
ants.sort()


# 2. TO SOLVE THE PROBLEM

# Let us think when the last ant falls.
# Think of collision as an intersection.
# Then, we only have to consider the leftmost ant that goes right and the rightmost and that goes left.

# Now, let us think which ant falls last.
# The number of ants that go left cannot change.
# If X ants go left at first, first X ants on a sorted array must fall left.

to_left_count = 0

to_left_max = 0
to_right_min = length

for loc, to_left, ant in ants:
    
    if to_left:
        to_left_count += 1
        to_left_max = max(to_left_max, loc)
    else:
        to_right_min = min(to_right_min, loc)

if to_left_max > (length - to_right_min):
    print(ants[to_left_count-1][2], to_left_max)
else:
    print(ants[to_left_count][2], length - to_right_min)