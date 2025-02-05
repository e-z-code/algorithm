'''
BOJ2159 - Cake Delivery (https://www.acmicpc.net/problem/2159)

You have to deliver cakes to N customers in the given order.
You can complete the delivery by visiting the cell adjacent to or where customers are.
Determine the minimum distance to complete all deliveries.
'''

# TIME COMPLEXITY : O(N)

import sys
inf = float('inf')


# 1. TO GET THE INPUT

customer_count = int(sys.stdin.readline())
start_x, start_y = map(int, sys.stdin.readline().split())

locations = []
for loc in range(customer_count):
    x, y = map(int, sys.stdin.readline().split())
    locations.append((x, y))


# 2. TO SOLVE THE PROBLEM
# dp[i][j] = Minimum distance to finish delivery to i-th location by arriving at j-th valid point.

dx = [0, -1, 0, 1, 0]
dy = [1, 0, 0, 0, -1]

dp = [[inf, inf, inf, inf, inf] for idx in range(customer_count)]

for i in range(customer_count):
    for j in range(5):
        
        dest_x = locations[i][0] + dx[j]
        dest_y = locations[i][1] + dy[j]
        
        if i == 0:
            dp[i][j] = abs(start_x - dest_x) + abs(start_y - dest_y)
        else:
            for k in range(5):
                src_x = locations[i-1][0] + dx[k]
                src_y = locations[i-1][1] + dy[k]
                dp[i][j] = min(dp[i][j], dp[i-1][k] + abs(src_x - dest_x) + abs(src_y - dest_y))

print(min(dp[-1]))