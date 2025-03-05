'''
BOJ10937 - Clocks (https://www.acmicpc.net/problem/10266)

Given the relative location of the needles of two clocks, determine if they are identical.
'''

# TIME COMPLEXITY : O(N log N)

import sys


# 1. TO GET THE INPUT

needle_count = int(sys.stdin.readline())

clockA = list(map(int, sys.stdin.readline().split()))
clockA.sort()

clockB = list(map(int, sys.stdin.readline().split()))
clockB.sort()


# 2. TO CALCULATE INTERVALS

intervalA = []
for idx in range(needle_count):
    if idx == 0:
        intervalA.append(clockA[idx] - clockA[idx-1] + 360000)
    else:
        intervalA.append(clockA[idx] - clockA[idx-1])
intervalA += intervalA

intervalB = []
for idx in range(needle_count):
    if idx == 0:
        intervalB.append(clockB[idx] - clockB[idx-1] + 360000)
    else:
        intervalB.append(clockB[idx] - clockB[idx-1])


# 3. TO SOLVE THE PROBLEM - KMP

kmp_table = [0 for idx in range(needle_count)]

# To construct a table

j = 0
for i in range(1, needle_count):
    while j > 0 and intervalB[i] != intervalB[j]:
        j = kmp_table[j-1]
    if intervalB[i] == intervalB[j]:
        j += 1
        kmp_table[i] = j

# To solve the problem

ans = "impossible"

j = 0
for i in range(needle_count * 2):
    while j > 0 and intervalA[i] != intervalB[j]:
        j = kmp_table[j-1]
    if intervalA[i] == intervalB[j]:
        j += 1
        if j == needle_count:
            ans = "possible"
            j = kmp_table[j-1]

print(ans)