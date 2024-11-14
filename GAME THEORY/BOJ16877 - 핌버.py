'''
BOJ16877 - Pimber (https://www.acmicpc.net/problem/16877)

Two players play the NIM game.
However, each player can only remove rocks of Fibonacci numbers.
Assuming each player makes the optimal move, determine who will win the game.
'''

# TIME COMPLEXITY : O(max(max(P), N))

import sys


# 1. TO CALCULATE FIBONACCI NUMBERS
# There are 31 fibonacci numbers that do not exceed 3000000.

fibonacci_nums = [1, 2]
while fibonacci_nums[-2] + fibonacci_nums[-1] <= 3000000:
    fibonacci_nums.append(fibonacci_nums[-2] + fibonacci_nums[-1])


# 2. TO CALCULATE THE GRUNDY NUMBER OF A PILE OF N ROCKS

grundy = [0 for rock_count in range(3000001)]

for rock_count in range(1, 3000001):
    
    next_state_grundy = set()
    for fibonacci_num in fibonacci_nums:
        if rock_count < fibonacci_num:
            break
        next_state_grundy.add(grundy[rock_count - fibonacci_num])
    
    result = 0
    while result in next_state_grundy:
        result += 1
    
    grundy[rock_count] = result


# 3. TO GET THE INPUT

pile_count = int(sys.stdin.readline())
piles = list(map(int, sys.stdin.readline().split()))


# 4. TO SOLVE THE PROBLEM
# Grundy number of multiple games can be obtained by XOR operation on grundy numbers of each game.

total_grundy = 0
    
for pile in piles:
    total_grundy ^= grundy[pile]

if total_grundy == 0:
    print("cubelover")
else:
    print("koosaga")