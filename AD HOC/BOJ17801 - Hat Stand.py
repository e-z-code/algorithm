'''
BOJ17801 - Hat Stand (https://www.acmicpc.net/problem/17801)

There is an array A and a plan.
You swap elements of the array according to the plan.
If the plan says A[X], you swap A[0] with A[X] with the cost of X.
Given that A[0] = C[0], find A that minimizes the cost.
'''

# TIME COMPLEXITY : O(max(N log N, C))

import sys


# 1. TO GET THE INPUT

hat_count, plan_length = map(int, sys.stdin.readline().split())
plan = list(map(int, sys.stdin.readline().split()))


# 2. TO COUNT HOW MANY TIME EACH RACK IS VISITED
# The number of visit to each rack depends on the initial value.

now_loc = [init_hat for init_hat in range(hat_count + 1)]
visit_count = [0 for init_hat in range(hat_count + 1)]

last_hat = plan[0]
for idx in range(1, plan_length):
    now_hat = plan[idx]
    visit_count[now_loc[now_hat]] += 1
    now_loc[last_hat], now_loc[now_hat] = now_loc[now_hat], now_loc[last_hat]
    last_hat = now_hat


# 3. TO SOLVE THE PROBLEM

key = []
for hat in range(1, hat_count + 1):
    if hat != plan[0]:
        key.append((visit_count[hat], hat))
key.sort(reverse=True)

ans_dist = 0
ans = []
for idx in range(hat_count - 1):
    count, hat = key[idx]
    ans_dist += count * (idx + 1)
    ans.append(str(hat))

print(ans_dist)
print(" ".join(ans))