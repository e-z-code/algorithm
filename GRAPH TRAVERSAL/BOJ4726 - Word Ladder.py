'''
BOJ4726 - Word Ladder (https://www.acmicpc.net/problem/4726)

There is the game "Word Ladder".
You start with a word and change one letter at a time until you reach a target word.
No word in the chain appears more than once.
You are good at the game and will always find the shortest ladder.
In this variation, you only have a limited vocabulary.
Determine the length of the longest word ladder you can find.
'''

# TIME COMPLEXITY : O(TSpow(N, 2)) [T : Number of test cases, S : Length of the longest string]

import sys
from collections import deque


# 3. BFS FUNCTION

def max_length(start):
    
    visited = [-1 for idx in range(word_count)]
    visited[start] = 1
    
    queue = deque([start])
    while queue:
        now_idx = queue.popleft()
        for next_idx in graph[now_idx]:
            if visited[next_idx] == -1:
                visited[next_idx] = visited[now_idx] + 1
                queue.append(next_idx)
    
    return max(visited)


# 1. TO GET THE INPUT

while True:
    
    word_count = int(sys.stdin.readline())
    if word_count == 0:
        break
    
    words = []
    for word in range(word_count):
        words.append(sys.stdin.readline().strip())
    words.sort(key = lambda x : len(x))
    
    
    # 2. CONNECT WORDS THAT CAN BE PLACED ADJACENTLY
    
    graph = {}
    for idx in range(word_count):
        graph[idx] = []
    
    for i in range(word_count):
        for j in range(i+1, word_count):
            
            wordA = words[i]
            wordB = words[j]
            
            if len(wordA) == len(wordB):
                
                different = 0
                
                for idx in range(len(wordA)):
                    if wordA[idx] != wordB[idx]:
                        different += 1
            
                if different <= 1:
                    graph[i].append(j)
                    graph[j].append(i)
            
            elif len(wordA) + 1 == len(wordB):
                
                wordA_idx = 0
                for wordB_idx in range(len(wordB)):
                    if wordA_idx != len(wordA) and wordA[wordA_idx] == wordB[wordB_idx]:
                        wordA_idx += 1
                
                if wordA_idx == len(wordA):
                    graph[i].append(j)
                    graph[j].append(i)
    
    
    # 4. TO SOLVE THE PROBLEM
    
    ans = 0
    for idx in range(word_count):
        ans = max(ans, max_length(idx))
    print(ans)