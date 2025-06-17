'''
BOJ27914 - Interview (https://www.acmicpc.net/problem/27914)

There are N students in a row.
You want to choose consecutive students of any number.
Answer Q queries: How many possible cases are there when considering first X students?
'''

# TIME COMPLEXITY : O(N)

import sys


# 1. TO GET THE INPUT

student_count, my_grade, query_count = map(int, sys.stdin.readline().split())
students_grade = list(map(int, sys.stdin.readline().split()))


# 2. TO GET ANSWERS FOR ALL QUERIES

# max_row[i] = How many students have different grades from i-th index

max_row = [0 for idx in range(student_count)]

for idx in range(student_count):
    
    if idx == 0:
        if my_grade == students_grade[idx]:
            continue
        else:
            max_row[idx] = 1
    else:
        if my_grade == students_grade[idx]:
            continue
        else:
            max_row[idx] = max_row[idx-1] + 1

# dp[i] = Possible number of cases when considering first i students
# dp[i] = dp[i-1] + max_row[i]

dp = [0 for idx in range(student_count)]

for idx in range(student_count):
    
    if idx == 0:
        dp[idx] = max_row[idx]
    else:
        dp[idx] = dp[idx-1] + max_row[idx]


# 3. TO SOLVE THE PROBLEM

queries = list(map(int, sys.stdin.readline().split()))

for query in queries:
    print(dp[query-1])