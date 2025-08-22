'''
CF2132D - From 1 to Infinity (https://codeforces.com/contest/2132/problem/D)

You wrote infinite sequence of digits that consists of the positive integers written consecutively.
Determine the sum of the digits until K-th digit.
'''

# TIME COMPLEXITY : O(T log K)

import sys


# 3. A FUNCTION TO CALCULATE THE SUM OF DIGITS UNTIL N

def sum_digits(last_num):
    
    last_num = str(last_num)
    digit_count = [0 for index in range(10)]

    for index in range(len(last_num)):
        
        digit = int(last_num[index])
        
        if index == 0:
            
            for num in range(1, 10):
                if num < digit:
                    digit_count[num] += pow(10, len(last_num) - index - 1)
                elif num == digit:
                    if len(last_num) != 1:
                        digit_count[num] += int("".join(last_num[1:])) + 1
                    else:
                        digit_count[num] += 1
                
        elif 0 < index < len(last_num) - 1:
            
            for num in range(10):
                digit_count[num] += int("".join(last_num[:index])) * pow(10, len(last_num) - index - 1)
                if num < digit:
                    digit_count[num] += pow(10, len(last_num) - index - 1)
                elif num == digit:
                    digit_count[num] += int("".join(last_num[index+1:])) + 1
            digit_count[0] -= pow(10, len(last_num) - index - 1)
        
        else:
            
            for num in range(10):
                digit_count[num] += int("".join(last_num[:index])) 
                if num <= digit:
                    digit_count[num] += 1
            digit_count[0] -= 1
    
    result = 0
    for num in range(1, 10):
        result += num * digit_count[num]
    return result


# 1. TO GET THE INPUT

test_count = int(sys.stdin.readline())

for test in range(test_count):
    
    last_digit = int(sys.stdin.readline())
    
    
    # 2. TO FIND THE LAST NUMBER AND REMAINING NUMBER OF DIGITS
    
    key_digits = [0]
    for digit in range(1, 20):
        key_digits.append(key_digits[-1] + 9 * pow(10, digit - 1) * digit)
    
    last_number = 0
    remainder = 0
    for digit in range(20):
        if last_digit < key_digits[digit]:
            last_number = pow(10, digit - 1) - 1
            last_digit -= key_digits[digit-1]
            last_number += last_digit // digit
            remainder = last_digit % digit
            break
    
    
    # 4. TO SOLVE THE PROBLEM
    
    ans = sum_digits(last_number)
    
    next_number = str(last_number + 1)
    for idx in range(remainder):
        ans += int(next_number[idx])
    
    print(ans)
    