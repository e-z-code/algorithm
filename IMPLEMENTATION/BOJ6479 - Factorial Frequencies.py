'''
BOJ6479 - Factorial Frequencies (https://www.acmicpc.net/problem/6479)

Given N, calculate how many times each digit appears in N!.
'''

# TIME COMPLEXITY : O(N)

import sys


# 1. TO CALCULATE FACTORIALS

factorial = [1]

for num in range(1, 367):
    factorial.append(factorial[-1] * num)


# 2. TO GET THE INPUT 

while True:
    
    num = int(sys.stdin.readline())
    if num == 0:
        break
    nothing = sys.stdin.readline().strip()
    
    
    # 3. TO SOLVE THE PROBLEM - FORMATTING
    
    count = [0 for digit in range(10)]
    
    val = str(factorial[num])
    for char in val:
        count[int(char)] += 1
    
    for digit in range(10):
        
        occurrence = count[digit]
        
        occurrence = str(occurrence)
        if len(occurrence) != 5:
            occurrence = " " * (5 - len(occurrence)) + occurrence
        
        count[digit] = occurrence
    
    print("{}! --".format(num))
    print("   (0){}    (1){}    (2){}    (3){}    (4){} ".format(count[0], count[1], count[2], count[3], count[4]))
    print("   (5){}    (6){}    (7){}    (8){}    (9){} ".format(count[5], count[6], count[7], count[8], count[9]))