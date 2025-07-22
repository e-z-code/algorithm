'''
BOJ26030 - Graduation Guarantee (https://www.acmicpc.net/problem/26030)

There are N questions in an exam.
You get +1 point if answered correctly, -1 point if answered wrong, and 0 points if unanswered.
You need K points to pass the exam.
Given the probability of making a correct guess for each question, determine the probability of passing the exam if you made an optimal move.
'''

# TIME COMPLEXITY : O(N^2)

import sys


# 1. TO GET THE INPUT

question_count, goal_score = map(int, sys.stdin.readline().split())
probs = list(map(float, sys.stdin.readline().split()))

probs.sort(reverse=True)


# 2. DYNAMIC PROGRAMMING
# You must make a guess from questions with higher probability.
# dp[i][j] = (Probability to get score j when making a guess until i-th question)

dp = [[0 for correct in range(question_count + 1)] for question in range(question_count + 1)]
dp[0][0] = 1

for question in range(question_count):
    
    prob = probs[question]
    question += 1
    
    for correct in range(question + 1):
        if correct == 0:
            dp[question][correct] = dp[question-1][correct] * (1 - prob)
        elif correct == question:
            dp[question][correct] = dp[question-1][correct-1] * prob
        else:
            dp[question][correct] = dp[question-1][correct-1] * prob + dp[question-1][correct] * (1 - prob)


# 3. TO SOLVE THE PROBLEM

ans = 0

for question in range(question_count + 1):
    now_prob = 0
    for correct in range(question + 1):
        wrong = question - correct
        if correct - wrong >= goal_score:
            now_prob += dp[question][correct]
    ans = max(ans, now_prob)

print(ans)