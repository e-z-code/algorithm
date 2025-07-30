'''
BOJ5095 - Matrix Powers (https://www.acmicpc.net/problem/5095)

There is a matrix of size N.
Multiply it P times.
'''

# TIME COMPLEXITY : O(N^3 log P) 

import sys


# 1. A FUNCTION FOR MATRIX POWER

def matrix_multiplication(matrixA, matrixB):
    
    result = [[0 for col in range(size)] for row in range(size)]
    
    for row in range(size):
        for col in range(size):
            for x in range(size):
                result[row][col] += matrixA[row][x] * matrixB[x][col]
                result[row][col] %= mod
    
    return result

def matrix_power(matrix, exp):
    
    if exp == 1:
        return matrix
    else:
        half_powered = matrix_power(matrix, exp // 2)
        if exp % 2 == 0:
            return matrix_multiplication(half_powered, half_powered)
        else:
            return matrix_multiplication(matrix_multiplication(half_powered, half_powered), matrix)


# 2. TO GET THE INPUT AND SOLVE THE PROBLEM

while True: 
    
    size, mod, exp = map(int, sys.stdin.readline().split())
    if size == 0 and mod == 0 and exp == 0:
        break

    matrix = []
    for row in range(size):
        matrix.append(list(map(int, sys.stdin.readline().split())))

    ans = matrix_power(matrix, exp)
    for row in ans:
        print(" ".join(map(str, row)))
    print()