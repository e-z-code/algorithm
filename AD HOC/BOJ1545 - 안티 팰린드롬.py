'''
BOJ1545 - Anti-palindrome (https://www.acmicpc.net/problem/1545)

A string of length N is an anti-palindrome if P[i] != P[N-i-1] for 0 <= i < (N-1)/2.
Given a string S, determine the lexicographically foremost anti-palindrome anagram of S.
If it does not exist, print -1.
'''

# TIME COMPLEXITY : O(|S|)

import sys


# 1. TO GET THE INPUT

word = sys.stdin.readline().strip()


# 2. TO CHECK WHETHER IT IS POSSIBLE
# If a character appears more than (N + 1) // 2 times, there is no anti-palindrome anagram. (Pigeonhole Principle)

possible = True

count = [0 for alphabet in range(26)]

for char in word:
    count[ord(char) - 97] += 1

for alphabet in range(26):
    if (len(word) + 1) // 2 < count[alphabet]:
        possible = False


# 3. TO CONSTRUCT THE ANSWER
# Greedily put alphabet from 'a' to 'z' from the front. 

if possible:
    
    ans = ["X" for idx in range(len(word))] # X = Unoccupied index

    for alphabet in range(26):
        idx = 0
        while count[alphabet]:
            if ans[idx] == "X" and ans[len(word) - idx - 1] != chr(alphabet + 97):
                ans[idx] = chr(alphabet + 97)
                count[alphabet] -= 1
            idx += 1

    print("".join(ans))

else:
    
    print(-1)