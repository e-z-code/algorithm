'''
BOJ5904 - Moo (https://www.acmicpc.net/problem/5904)

Let S(0) = "moo" and S(k) = S(k-1) + "m" + "o" * (k + 2) + S(k-1).
Calculate the N-th character.
'''

# TIME COMPLEXITY : O(log N)

import sys


# 2. A FUNCTION TO SOLVE THE PROBLEM
# The function returns n-th character of S(k).

def solve(k, n):
    
    if k == 0:
        if n == 1:
            return "m"
        else:
            return "o"
    else:
        if n <= words_length[k-1]:
            return solve(k-1, n)
        elif n == words_length[k-1] + 1:
            return "m"
        elif n <= words_length[k-1] + k + 3:
            return "o"
        else:
            return solve(k-1, n - words_length[k-1] - k - 3)


# 1. TO GET THE LENGTH OF EACH WORD

words_length = [3]

while words_length[-1] <= 10 ** 9:
    words_length.append(words_length[-1] * 2 + len(words_length) + 3)


# 3. TO GET THE INPUT AND SOLVE THE PROBLEM

loc = int(sys.stdin.readline())

print(solve(len(words_length), loc))