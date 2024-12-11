'''
BOJ4865 - Shortest Prefixes (https://www.acmicpc.net/problem/4865)

Given a list of N words, for each word, determine the shortest prefix that uniquely identifies the word.
'''

# TIME COMPLEXITY : O(N^2|S|^2) 
# |S| = The maximum length of the word

import sys


# 1. TO GET THE INPUT

words = []
words_prefix = []

while True:
    
    try:
        
        word = sys.stdin.readline().strip()
        words.append(word)
        
        word_prefix = []
        for idx in range(1, len(word) + 1):
            word_prefix.append(word[:idx])
        words_prefix.append(word_prefix)
        
        if len(word) == 0:
            break
        
    except:
        
        break


# 2. TO SOLVE THE PROBLEM

for i in range(len(words)):
    
    word = words[i]
    word_prefix = words_prefix[i]
    
    for prefix in word_prefix:
        
        if len(prefix) == len(word):
            print(word, word)
            break
        
        id = True
        
        for j in range(len(words)):
            target = words[j]
            target_prefix = words_prefix[j]
            if word != target and prefix in target_prefix:
                id = False
                break
        
        if id:
            print(word, prefix)
            break