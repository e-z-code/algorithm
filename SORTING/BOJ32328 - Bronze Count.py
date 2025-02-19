'''
BOJ16173 - Jump King Jelly (Small) (https://www.acmicpc.net/problem/16173)

There are N participants.
Given their scores, determine the third-highest score and the number of participants who got that score.
'''

# TIME COMPLEXITY : O(N log N)


import sys


# 1. TO GET THE INPUT

people_count = int(sys.stdin.readline())

scores = []
for score in range(people_count):
    scores.append(int(sys.stdin.readline()))


# 2. TO SOLVE THE PROBLEM

bronze_score = sorted(list(set(scores)))[-3]

print(bronze_score, scores.count(bronze_score))