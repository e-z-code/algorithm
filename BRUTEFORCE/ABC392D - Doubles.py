'''
ABC392D - Doubles (https://atcoder.jp/contests/abc392/tasks/abc392_d)

There are N dice.
Choose two dice with the maximum probability that the two dice show the same number.
'''

# TIME COMPLEXITY: O(K) [K = sum(K[i])]

import sys
from fractions import Fraction


# 1. TO GET THE INPUT

dice_count = int(sys.stdin.readline())

dice_size = [0 for dice in range(dice_count)]
dice_nums = [{} for dice in range(dice_count)]

for dice in range(dice_count):
    
    info = list(map(int, sys.stdin.readline().split()))
    
    dice_size[dice] = info[0]
    for idx in range(1, len(info)):
        dice_nums[dice][info[idx]] = dice_nums[dice].get(info[idx], 0) + 1


# 2. BRUTE-FORCE

ans = Fraction(0, 1)

for i in range(dice_count):
    for j in range(i+1, dice_count):
        
        result = 0
        
        diceA_num_count = len(dice_nums[i])
        diceB_num_count = len(dice_nums[j])
        
        if diceA_num_count <= diceB_num_count:
            for num in dice_nums[i]:
                result += dice_nums[i][num] * dice_nums[j].get(num, 0)
        else:
            for num in dice_nums[j]:
                result += dice_nums[j][num] * dice_nums[i].get(num, 0)
        
        ans = max(ans, Fraction(result, dice_size[i] * dice_size[j]))

print(float(ans))