'''
BOJ20287 - Lavaspar (https://www.acmicpc.net/problem/20287)

You are given a word search board and N words to search.
In this game, you can find the word S by finding S or one of its anagrams. 
A cell is a special cell if the cell belongs to two or more words.
Determine the number of special cells. 
'''

# TIME COMPLEXITY : O(LCN|P|)

import sys


# 2. A FUNCTION TO CHECK ANAGRAM
# To check every anagram for a word of length N costs O(N!).
# The following method costs O(N). 

def is_anagram(wordA, wordB):
    
    countA = [0 for alphabet in range(26)]
    for char in wordA:
        countA[ord(char) - 65] += 1
    
    countB = [0 for alphabet in range(26)]
    for char in wordB:
        countB[ord(char) - 65] += 1
    
    if countA == countB:
        return True
    else:
        return False


# 1. TO GET THE INPUT

row_count, col_count = map(int, sys.stdin.readline().split())

board = []
for row in range(row_count):
    row_input = list(sys.stdin.readline().strip())
    board.append(row_input)

word_count = int(sys.stdin.readline())

words = []
for idx in range(word_count):
    word = sys.stdin.readline().strip()
    words.append(word)


# 3. TO CHECK ALL ANAGRAM APPEARANCE

anagram_of = [[set() for col in range(col_count)] for row in range(row_count)]

for row in range(row_count):
    for col in range(col_count):
        for idx in range(word_count):
            
            word = words[idx]
            
            # Vertical
            if row + len(word) <= row_count:
                
                new_word = []
                for dy in range(len(word)):
                    new_word.append(board[row + dy][col])
                new_word = "".join(new_word)
                
                if is_anagram(word, new_word):
                    for dy in range(len(word)):
                        anagram_of[row + dy][col].add(idx)
            
            # Horizontal
            if col + len(word) <= col_count:
                
                new_word = []
                for dx in range(len(word)):
                    new_word.append(board[row][col + dx])
                new_word = "".join(new_word)
                
                if is_anagram(word, new_word):
                    for dx in range(len(word)):
                        anagram_of[row][col + dx].add(idx)

            # Diagonal (Right)
            if row + len(word) <= row_count and col + len(word) <= col_count:
                
                new_word = []
                for delta in range(len(word)):
                    new_word.append(board[row + delta][col + delta])
                new_word = "".join(new_word)

                if is_anagram(word, new_word):
                    for delta in range(len(word)):
                        anagram_of[row + delta][col + delta].add(idx)
            
            # Diagonal (Left)
            if row + len(word) <= row_count and 0 <= col - len(word) + 1:
                
                new_word = []
                for delta in range(len(word)):
                    new_word.append(board[row + delta][col - delta])
                new_word = "".join(new_word)
                
                if is_anagram(word, new_word):
                    for delta in range(len(word)):
                        anagram_of[row + delta][col - delta].add(idx)


# 4. TO SOLVE THE PROBLEM

ans = 0

for row in range(row_count):
    for col in range(col_count):
        if len(anagram_of[row][col]) > 1:
            ans += 1

print(ans)