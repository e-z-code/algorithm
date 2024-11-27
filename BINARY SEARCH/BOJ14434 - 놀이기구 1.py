'''
BOJ14434 - Ride (https://www.acmicpc.net/problem/14434)

There are N kids and M rides in an amusement park.
You are given Q queries (i, j, k): kids i and j want to take a ride k.
To take a ride, the sum of the heights of two kids should not be shorter than the height limit of k.
Initially, all kids are 0.
However, one of the kids grows by 1cm every day.
Determine how many rides the kids take each day.
'''

# TIME COMPLEXITY : O(Q log ^ 2 K)

import sys
from bisect import bisect_right


# 1. TO GET THE INPUT

kid_count, ride_count, day_count, query_count = map(int, sys.stdin.readline().split())
min_height = list(map(int, sys.stdin.readline().split()))

growth = list(map(int, sys.stdin.readline().split()))

kid_info = [[] for kid in range(kid_count + 1)] # Store when the kid grows
for day in range(day_count):
    kid_info[growth[day]].append(day + 1)


# 2. PROCESS QUERIES 

prefix_sum = [0 for day in range(day_count + 1)]

for query in range(query_count):
    
    kidA, kidB, ride = map(int, sys.stdin.readline().split())
    ride -= 1
    
    kidA_max_height = len(kid_info[kidA])
    kidB_max_height = len(kid_info[kidB])
    if kidA_max_height + kidB_max_height >= min_height[ride]:
        
        # Binary search - When kids i and j take a ride for the first time
        
        left = 0
        right = day_count
        
        while left + 1 < right:
            
            mid = (left + right) // 2
            
            kidA_height = bisect_right(kid_info[kidA], mid)
            kidB_height = bisect_right(kid_info[kidB], mid)
            
            if kidA_height + kidB_height < min_height[ride]:
                left = mid
            else:
                right = mid
        
        prefix_sum[right] += 1


# 3. TO SOLVE THE ANSWER
# If kids i and j can take a ride at day X, they can take a ride at day X+1.

for day in range(1, day_count + 1):
    
    prefix_sum[day] += prefix_sum[day-1]
    print(prefix_sum[day])