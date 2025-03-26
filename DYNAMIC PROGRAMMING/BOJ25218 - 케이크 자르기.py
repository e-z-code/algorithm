'''
BOJ25218 - Cut the Cake (https://www.acmicpc.net/problem/25218)

There is an R X C cake. Each cell has a topping.
You cut the cake N-1 times horizontally or vertically to share with N friends.
You must give each friend a piece that includes the friend's favorite topping.
Determine the number of possible cases.
'''

# TIME COMPLEXITY : O(NRC(R+C))


import sys
MOD = pow(10, 9) + 7
sys.setrecursionlimit(10 ** 5)


# 3. EFFICIENT FUNCTION TO CHECK WHETHER A TOPPING EXISTS

def exist(rowA, colA, rowB, colB, target):
    
    result = 0
    
    result += prefix_sum[rowB][colB][target]
    if rowA != 0:
        result -= prefix_sum[rowA-1][colB][target]
    if colA != 0:
        result -= prefix_sum[rowB][colA-1][target]
    if rowA != 0 and colA != 0:
        result += prefix_sum[rowA-1][colA-1][target]
    
    if result > 0:
        return True
    else:
        return False


# 5. A FUNCTION TO FILL DP TABLE

def fill_table(row, col, friend):
    
    if dp[row][col][friend] != -1:
        return dp[row][col][friend]

    result = 0
    for new_row in range(row+1, row_count):
        if exist(row, col, new_row-1, col_count-1, topping_to_num[goal[friend]]):
            result += fill_table(new_row, col, friend+1)
            result %= MOD
    for new_col in range(col+1, col_count):
        if exist(row, col, row_count-1, new_col-1, topping_to_num[goal[friend]]):
            result += fill_table(row, new_col, friend+1)
            result %= MOD
    
    dp[row][col][friend] = result
    return result


# 1. TO GET THE INPUT

test_count = int(sys.stdin.readline())

for test in range(test_count):
    
    row_count, col_count, friend_count = map(int, sys.stdin.readline().split())
    
    grid = []
    for row in range(row_count):
        grid.append(list(sys.stdin.readline().strip()))
    goal = list(sys.stdin.readline().strip())

    topping_to_num = {'S':0, 'B':1, 'R':2, '.':3}


    # 2. PREFIX SUM

    prefix_sum = [[[0, 0, 0, 0] for col in range(col_count)] for row in range(row_count)]
    
    for row in range(row_count):
        for col in range(col_count):
            prefix_sum[row][col][topping_to_num[grid[row][col]]] += 1
    
    for row in range(row_count):
        for col in range(col_count):
            for topping in range(4):
                
                if row != 0:
                    prefix_sum[row][col][topping] += prefix_sum[row-1][col][topping]
                if col != 0:
                    prefix_sum[row][col][topping] += prefix_sum[row][col-1][topping]
                if row != 0 and col != 0:
                    prefix_sum[row][col][topping] -= prefix_sum[row-1][col-1][topping]
    
    
    # 4. BASE CASE
    # DP[i][j][k] = Number of possible cases when considering from k-th friends and the upper-leftmost cell is (i, j).
    
    dp = [[[-1 for friend in range(friend_count)] for col in range(col_count)] for row in range(row_count)]
    
    for row in range(row_count):
        for col in range(col_count):
            
            if exist(row, col, row_count-1, col_count-1, topping_to_num[goal[friend_count-1]]):
                dp[row][col][friend_count-1] = 1
            else:
                dp[row][col][friend_count-1] = 0
    
    
    # 6. TO SOLVE THE PROBLEM
    
    print(fill_table(0, 0, 0))