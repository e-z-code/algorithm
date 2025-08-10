'''
ABC418B - You're a teapot (https://atcoder.jp/contests/abc418/tasks/abc418_b)

If a string X begins with and ends with T, its filling rate equals the ratio of T.
Otherwise, the filling rate is 0.
Given a string S, find the maximum possible filling rate of a substring of S.
'''

# TIME COMPLEXITY: O(pow(|S|, 2))

import sys


# 1. TO GET THE INPUT AND SOLVE THE PROBLEM

string = sys.stdin.readline().strip()

ans = 0
for i in range(len(string)):
    for j in range(i+1, len(string)):
        substring = string[i:j+1]
        if len(substring) >= 3 and string[i] == string[j] == "t":
            ans = max(ans,  (substring.count("t") - 2) / (len(substring) - 2))

print(ans)