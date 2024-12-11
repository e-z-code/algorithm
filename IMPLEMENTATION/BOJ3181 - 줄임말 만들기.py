'''
BOJ3181 - Abbreviation (https://www.acmicpc.net/problem/3181)

Given a sentence of N words, you create an abbreviation by taking the first letter of each word except for some special words.
However, if a special word is the first word, you must include it.
Determine the abbreviation.
'''

# TIME COMPLEXITY : O(N^2)

import sys


# 1. TO GET THE INPUT

special_words = ["i", "pa", "te", "ni", "niti", "a", "ali", "nego", "no", "ili"]
words = list(sys.stdin.readline().strip().split())


# 2. TO SOLVE THE PROBLEM

abbr = ""

for idx in range(len(words)):
    
    word = words[idx]
    
    if idx != 0:
        if word in special_words:
            continue
    
    abbr += word[0].upper()

print(abbr)