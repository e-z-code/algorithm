'''
BOJ16523 - Cheap Trips (https://www.acmicpc.net/problem/16523)

In your country, when the first trip of a passenger starts, a 120-minute interval for discounts also starts.
The discount for the second trip is 50%.
The discount for trips up to the sixth trip is 75%.
Determine the minimum cost to complete all the given trips in the order.
'''

# TIME COMPLEXITY : O(N)

import sys
inf = float('inf')


# 1. TO GET THE INPUT

trip_count = int(sys.stdin.readline())

trip_time = []
trip_cost = []

for trip in range(trip_count):
    time, cost = map(int, sys.stdin.readline().split())
    trip_time.append(time)
    trip_cost.append(cost)


# 2. TO SOLVE THE PROBLEM
# dp[i][j] = The minimum cost when going i-th trip for j-th discount

dp = [[inf for order in range(6)] for trip in range(trip_count)]
dp[0][0] = trip_cost[0]

for trip in range(1, trip_count):
    for order in range(6):
        if order <= trip and sum(trip_time[trip-order:trip]) < 120:
            if order == 0:
                dp[trip][order] = min(dp[trip-1]) + trip_cost[trip]
            elif order == 1:
                dp[trip][order] = dp[trip-1][0] + trip_cost[trip] * 0.5
            else:
                dp[trip][order] = dp[trip-order][0] + trip_cost[trip-order+1] * 0.5 + sum(trip_cost[trip-order+2:trip+1]) * 0.25

print(format(min(dp[-1]), ".2f"))