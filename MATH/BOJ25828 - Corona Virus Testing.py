'''
BOJ25828 - Corona Virus Testing (https://www.acmicpc.net/problem/25828)

You test the corona-virus.
The simplest way is to test all individuals.
Instead, you can test only one person per group and, if the one is positive, re-test the whole group.
Determine which method spends more kits.
'''

# TIME COMPLEXITY : O(1)

import sys


# 1. TO GET THE INPUT

group_count, people_in_group, positive_group_count = map(int, sys.stdin.readline().split())


# 2. TO SOLVE THE PROBLEM

individual_test = group_count * people_in_group
group_test = group_count + positive_group_count * people_in_group

if individual_test < group_test:
    print(1)
elif individual_test == group_test:
    print(0)
else:
    print(2)