'''
BOJ16906 - Wookje Language (https://www.acmicpc.net/problem/16906)

In the Wookje language, every word consists of 0 and 1, and no word can be a prefix of another word.
Given the lengths of each word, determine if you can construct a list of distinct words in the Wookje language.
If it is possible, print each word.
'''

# TIME COMPLEXITY : O(max(S) ^ 2)
# S = Word length

import sys


# 1. TO GET THE INPUT

word_count = int(sys.stdin.readline())
word_length = list(map(int, sys.stdin.readline().split()))

word_info = []
for idx in range(word_count):
    word_info.append((word_length[idx], idx))
word_info.sort()


# 2. TO CONSTRUCT WORDS

possible = True
words = ["0" for idx in range(word_count)]

word = ""

# Start from the shortest length
for idx in range(word_count):
    
    length, loc = word_info[idx]
    
    if len(word) <= length:
        
        # Add 0s to the word
        word += "0" * (length - len(word))
        words[loc] = word
        
        # Add 1 to the value of the word and make it a new prefix
        word = bin(int(word, 2) + 1)[2:]
        if idx == word_count - 1 or len(word) <= length:
            word = "0" * (length - len(word)) + word
        else: # If it leads to overflow, then it implies every possible prefix has been used.
            possible = False
            break


# 3. TO SOLVE THE PROBLEM

if possible:
    print(1)
    for word in words:
        print(word)
else:
    print(-1)