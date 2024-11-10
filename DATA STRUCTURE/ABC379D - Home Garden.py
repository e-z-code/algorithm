'''
ABC379D - Home Garden (https://atcoder.jp/contests/abc379/tasks/abc379_d)

There are an infinite number of flower pots.
Process three types of queries as follows.

(1) Put a plant of height 0 in an empty flower pot.
(2) Wait for T days. The height of every plant increases by T.
(3) Harvest all plants with a height of at least H. Output the number of harvested plants.
'''

# TIME COMPLEXITY : O(Q)

import sys
from collections import deque


# 1. TO GET THE INPUT

query_count = int(sys.stdin.readline())


# 2. TO SOLVE THE PROBLEM

records = deque([]) # Record the time a plant entered the pot

now_time = 0
for query_input in range(query_count):
    
    query = list(map(int, sys.stdin.readline().split()))
    
    # Put
    if query[0] == 1:
        records.append(now_time)
    # Wait
    elif query[0] == 2:
        time = query[1]
        now_time += time
    # Harvest
    # Note that the order of harvest follows the principle of FIFO (First In First Out).
    else:
        height = query[1]
        harvested_count = 0
        while records and now_time - records[0] >= height:
            harvested_count += 1
            records.popleft()
        print(harvested_count)