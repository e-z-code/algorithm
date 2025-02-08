'''
ABC392C - Bib (https://atcoder.jp/contests/abc392/tasks/abc392_c)

There are N people numbered from 1 to N.
A person X is wearing a bib with the number Q[X] and is staring at person P[X].
For each bib, find the number written on the bib of the person that the person wearing the bib is staring at.
'''

# TIME COMPLEXITY: O(N)

import sys


# 1. TO GET THE INPUT

people_count = int(sys.stdin.readline())

looking_at = list(map(int, sys.stdin.readline().split()))
bibs = list(map(int, sys.stdin.readline().split()))


# 2. TO SOLVE THE PROBLEM

ans = [0 for person in range(people_count)]

for person in range(people_count):
    
    bib = bibs[person] - 1
    ans[bib] = bibs[looking_at[person] - 1]

print(" ".join(map(str, ans)))