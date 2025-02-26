'''
BOJ27980 - String Game (https://www.acmicpc.net/problem/27980)

A string X is written on a board. You have a string Y.
You put your string at any point on a board.
First, you compare the first letter of Y and the letter on the cell.
Then, you compare the next letter with the letter on either the left or right of the latest cell.
If the letter matches, you get a point.
Determine the maximum point you can get. 
'''

# TIME COMPLEXITY : O(NM)

import sys


# 1. TO GET THE INPUT

lengthA, lengthB = map(int, sys.stdin.readline().split())

stringA = sys.stdin.readline().strip()
stringB = sys.stdin.readline().strip()


# 2. TO SOLVE THE PROBLEM
# DP[j][i] = The maximum point when matching A[i] with B[j].

dp = [[0 for idxA in range(lengthA)] for idxB in range(lengthB)]

for idxB in range(lengthB):
    for idxA in range(lengthA):
        
        if idxB == 0:
            
            if stringA[idxA] == stringB[idxB]:
                dp[idxB][idxA] = 1
            else:
                dp[idxB][idxA] = 0
        
        else:
            
            if stringA[idxA] == stringB[idxB]:
                
                if idxA != 0:
                    dp[idxB][idxA] = max(dp[idxB-1][idxA-1] + 1, dp[idxB][idxA])
                if idxA != lengthA - 1:
                    dp[idxB][idxA] = max(dp[idxB-1][idxA+1] + 1, dp[idxB][idxA])
            
            else:
                
                if idxA != 0:
                    dp[idxB][idxA] = max(dp[idxB-1][idxA-1], dp[idxB][idxA])
                if idxA != lengthA - 1:
                    dp[idxB][idxA] = max(dp[idxB-1][idxA+1], dp[idxB][idxA])

print(max(dp[-1]))