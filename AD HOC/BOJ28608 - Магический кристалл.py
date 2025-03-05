'''
BOJ28608 - Magic Crystal (https://www.acmicpc.net/problem/28608)

Given X, you want to create two arithmetic expressions.
A is the product of all terms of an addition that results in X.
B is the sum of all terms of a multiplication that results in X.
Construct an addition and a multiplication such that A = B.
'''

# TIME COMPLEXITY : O(N)

import sys


# 1. TO GET THE INPUT

target_num = int(sys.stdin.readline())


# 2. TO SOLVE THE PROBLEM
# The key is to fill 1 for A.

if target_num < 4:
    
    print(-1, -1)

else:
    
    if target_num % 2 == 0:
        
        if target_num == 4:
            
            resultA = [2, 2]
            resultB = [4]
        
        else:
            
            resultB = [2, target_num // 2]
            energyB = 2 + target_num // 2
            
            resultA = [energyB]
            for count in range(target_num - energyB):
                resultA.append(1)
        
    else:
        
        resultB = [1, target_num]
        energyB = 1 + target_num
        
        resultA = [2, energyB // 2]
        for count in range(target_num - (energyB // 2 + 2)):
            resultA.append(1)
    
    print(len(resultA), len(resultB))
    print(" ".join(list(map(str, resultA))))
    print(" " .join(list(map(str, resultB))))