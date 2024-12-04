'''
BOJ27621 - Sum of Three Cubes (https://www.acmicpc.net/problem/27621)

For 0 <= N < 50, you are given a pair (X, Y, Z) such that X^2 + Y^2 + Z^2 = N.
Given N, print a (X, Y, Z) pair such that X^2 + Y^2 + Z^2 = N.
'''

# TIME COMPLEXITY : O(1)

import sys


# 1. PREPROCESSING

x = [0, 0, 0, 1, -1, -1, -1, 0, 0, 0, 1, -2, 7, -1, -1, -1, -511, 1, -1, 0, 1, -11, -1, -1, -2901096694, -1, 0, 0, 0, 1, -283059965, -1, -1, 8866128975287528, -1, 0, 1, 0, 1, 117367, -1, -1, -80538738812075974, 2, -5, 2, -2, 6, -23, -1]
y = [0, 0, 1, 1, -1, -1, -1, -1, 0, 1, 1, -2, 10, -1, -1, 2, -1609, 2, -2, -2, -2, -14, -1, -1, -15550555555, -1, -1, 0, 1, 1, -2218888517, -1, -1, -8778405442862239, 2, 2, 2, -3, -3, 134476, -1, -1, 80435758145817515, 2, -7, -3, 3, 7, -26, -1]
z = [0, 1, 1, 1, -1, -1, 2, 2, 2, 2, 2, 3, -11, -1, -1, 2, 1626, 2, 3, 3, 3, 16, -1, -1, 15584139827, 3, 3, 3, 3, 3, 2220422932, -1, -1, -2736111468807040, 3, 3, 3, 4, 4, -159380, -1, -1, 12602123297335631, 3, 8, 4, 3, -8, 31, -1]


# 2. TO SOLVE THE PROBLEM

num = int(sys.stdin.readline())

if x[num] == -1 and y[num] == -1 and z[num] == -1:
    print(0)
else:
    print(x[num], y[num], z[num])