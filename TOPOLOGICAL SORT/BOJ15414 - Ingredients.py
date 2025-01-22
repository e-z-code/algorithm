'''
BOJ15414 - Ingredients (https://www.acmicpc.net/problem/15414)

There are N pizza recipes that are additive.
Given budget B, choose pizzas such that the sum of prestige is the maximum.
'''

# TIME COMPLEXITY : O(NB)

import sys
from collections import deque
inf = float('inf')


# 1. TO GET THE INPUT

budget = int(sys.stdin.readline())
recipe_count = int(sys.stdin.readline())

graph = {}
in_degree = {}

for recipe in range(recipe_count):
    
    result, base, ingredient, added_cost, added_benefit = sys.stdin.readline().strip().split()
    added_cost = int(added_cost)
    added_benefit = int(added_benefit)
    
    if base in graph:
        graph[base].append((result, added_cost, added_benefit))
    else:
        graph[base] = [(result, added_cost, added_benefit)]
    graph[result] = graph.get(result, [])
    
    in_degree[result] = in_degree.get(result, 0) + 1


# 2. TOPOLOGICAL SORT

cost = {}
benefit = {}

t_sort = deque([])
for pizza in graph:
    if pizza not in in_degree:
        t_sort.append(pizza)
        cost[pizza] = 0
        benefit[pizza] = 0

while t_sort:
    now_pizza = t_sort.popleft()
    for next_pizza, added_cost, added_benefit in graph[now_pizza]:
        
        total_cost = cost[now_pizza] + added_cost
        total_benefit = benefit[now_pizza] + added_benefit
        if total_cost < cost.get(next_pizza, inf) or (total_cost == cost.get(next_pizza, inf) and total_benefit > benefit.get(next_pizza, 0)):
            cost[next_pizza] = total_cost
            benefit[next_pizza] = total_benefit
        
        in_degree[next_pizza] -= 1
        if in_degree[next_pizza] == 0:
            t_sort.append(next_pizza)


# 3. KNAPSACK DP

item = [(-1, -1)]
for pizza in cost:
    item.append((cost[pizza], benefit[pizza]))

dp = [[0 for cost in range(budget + 1)] for item in range(len(item))]

for idx in range(1, len(item)):
    for cost in range(budget + 1):
        
        dp[idx][cost] = dp[idx-1][cost]
        if item[idx][0] <= cost:
            dp[idx][cost] = max(dp[idx][cost], dp[idx-1][cost-item[idx][0]] + item[idx][1])


# 4. TO SOLVE THE PROBLEM

ans_benefit = 0
ans_cost = 0

for cost in range(budget + 1):
    if ans_benefit < dp[-1][cost]:
        ans_benefit = dp[-1][cost]
        ans_cost = cost

print(ans_benefit)
print(ans_cost)