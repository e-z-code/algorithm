'''
BOJ5053 - Cuckoo Hashing (https://www.acmicpc.net/problem/5053)

There are N elements.
For each element X, you know its hash values H1(X) and H2(X).
Given the size of the hash table, determine if all elements can be placed.
'''

# TIME COMPLEXITY : O(M(M + N))

import sys


# 2. A FUNCTION FOR BIPARTITE MATCHING

def bipartite_matching(word):
    
    if visited[word]:
        return False
    visited[word] = 1
    
    result = False
    
    for cell in graph[word]:
        if assigned[cell] == -1 or bipartite_matching(assigned[cell]):
            assigned[cell] = word
            result = True
            break
    
    return result


# 1. TO GET THE INPUT

test_count = int(sys.stdin.readline())

for test in range(test_count):
    
    word_count, cell_count = map(int, sys.stdin.readline().split())
    
    graph = {}
    for word in range(word_count):
        possible_cell = list(set(map(int, sys.stdin.readline().split())))
        graph[word] = possible_cell
    
    assigned = [-1 for cell in range(cell_count)]


    # 3. TO SOLVE THE PROBLEM
    
    for word in range(word_count):
        visited = [0 for word in range(word_count)]
        bipartite_matching(word)
    
    count = 0
    for cell in assigned:
        if cell != -1:
            count += 1

    # If all elements are assigned, the hashing is successful.
    if count == word_count:
        print("successful hashing")
    else:
        print("rehash necessary")