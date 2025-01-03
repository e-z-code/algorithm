'''
BOJ21322 - Rotate a Grid (https://www.acmicpc.net/problem/21322)

Given an N X N grid consisting of N // 2 conveyor belts, answer three types of queries.

(1) Rotate the A-th outside conveyor belt by B.
(2) Rotate 2 X 2 grid - (C, D), (C, D+1), (C+1, D+1), (C+1, D).
(3) Print the number on (E, F).
'''

# TIME COMPLEXITY : O(max(N^2, M))

import sys


# 2. A FUNCTION TO CHANGE ABSOLUTE LOCATION TO RELATIVE LOCATION
# Given (R, C), the function returns in what belt and where the cell is located. 

def convert(row, col):
    
    belt = size // 2 - max(abs(int(row - (size + 1) / 2)), abs(int(col - (size + 1) / 2)))
    belt_size = size + 2 - 2 * belt
    
    if row == belt:
        idx = col - belt + 1
    else:
        idx = belt_size
        if col == belt + belt_size - 1:
            idx += row - belt
        else:
            idx += belt_size - 1
            if row == belt + belt_size - 1:
                idx += belt + belt_size - 1 - col
            else:
                idx += belt_size - 1
                idx += belt + belt_size - 1 - row
    
    return belt, idx


# 1. TO GET THE INPUT

size, query_count = map(int, sys.stdin.readline().split())

grid = []
for row in range(size):
    grid.append(list(map(int, sys.stdin.readline().split())))


# 3. GROUP INPUT BY BELTS

start = [0 for idx in range(size // 2 + 1)] # Stores the index at the top-left cell of the belt. 
belts = [[-1 for idx in range(4 * size + 1)] for belt in range(size // 2 + 1)] # Stores each belt

for row in range(size):
    for col in range(size):
        belt, idx = convert(row+1, col+1)
        belts[belt][idx-1] = grid[row][col]

for belt in range(len(belts)):
    while len(belts[belt]) != 0 and belts[belt][-1] == -1:
        belts[belt].pop()


# 3. TO SOLVE THE PROBLEM

for query in range(query_count):
    
    query_type, numA, numB = map(int, sys.stdin.readline().split())
    
    if query_type == 1:
        
        belt, rotate = numA, numB
        start[belt] = (start[belt] - rotate) % len(belts[belt])
        
    elif query_type == 2:
        
        row, col = numA, numB
        
        beltA, idxA = convert(row, col)
        idxA = (start[beltA] + idxA - 1) % len(belts[beltA])
        beltB, idxB = convert(row, col + 1)
        idxB = (start[beltB] + idxB - 1) % len(belts[beltB])
        beltC, idxC = convert(row + 1, col + 1)
        idxC = (start[beltC] + idxC - 1) % len(belts[beltC])
        beltD, idxD = convert(row + 1, col)
        idxD = (start[beltD] + idxD - 1) % len(belts[beltD])
        
        belts[beltA][idxA], belts[beltB][idxB], belts[beltC][idxC], belts[beltD][idxD] = belts[beltD][idxD], belts[beltA][idxA], belts[beltB][idxB], belts[beltC][idxC]
    
    else:
        
        row, col = numA, numB
        
        belt, idx = convert(row, col)
        idx = (start[belt] + idx - 1) % len(belts[belt])
        print(belts[belt][idx])