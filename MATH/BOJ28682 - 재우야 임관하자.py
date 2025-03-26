'''
BOJ26862 - Commission Ceremony (https://www.acmicpc.net/problem/28682)

You play 1500 Monty Hall games.
Win at least 900 games.
'''

# TIME COMPLEXITY : O(N)


import sys


# 1. TO GET THE INPUT

choice_count = int(sys.stdin.readline())


# 2. TO SOLVE THE PROBLEM
# It is known that to change the choice is a right strategy.

ans = ["soccer" for choice in range(choice_count)]

print(" ".join(ans))
sys.stdout.flush()

response = list(sys.stdin.readline().strip().split())
for choice in range(choice_count):
    if response[choice] == "swimming":
        ans[choice] = "bowling"
    else:
        ans[choice] = "swimming"

print(" ".join(ans))
sys.stdout.flush()