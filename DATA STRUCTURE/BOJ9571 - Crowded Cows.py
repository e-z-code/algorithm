'''
BOJ9571 - Crowded Cows (https://www.acmicpc.net/problem/9571)

There are N cows. Cow i is stands location X[i] and has height H[i].
A cow i is crowded if there is another cow at least twice her height at both [X[i] - D, X[i]) and (X[i], X[i] + D].
Calculate the number of crowded cows.
'''

# TIME COMPLEXITY : O(N log N)

import sys, heapq


# 1. TO GET THE INPUT

cow_count, dist = map(int, sys.stdin.readline().split())

cows = []
for cow in range(cow_count):
    loc, height = map(int, sys.stdin.readline().split())
    cows.append((loc, height))
cows.sort()


# 2. TO SOLVE THE PROBLEM

check = [0 for idx in range(cow_count)]

# From front to back

heap = []

for idx in range(cow_count):
    loc, height = cows[idx]
    while len(heap) != 0:
        shortest_height, shortest_loc, shortest_idx = heap[0]
        if shortest_height * 2 <= height:
            if loc - dist <= shortest_loc:
                check[shortest_idx] += 1
            heapq.heappop(heap)
        else:
            break
    heapq.heappush(heap, (height, loc, idx))

# From back to front

heap = []

for idx in range(cow_count - 1, -1, -1):
    loc, height = cows[idx]
    while len(heap) != 0:
        shortest_height, shortest_loc, shortest_idx = heap[0]
        if shortest_height * 2 <= height:
            if shortest_loc <= loc + dist:
                check[shortest_idx] += 1
            heapq.heappop(heap)
        else:
            break
    heapq.heappush(heap, (height, loc, idx))

print(check.count(2))