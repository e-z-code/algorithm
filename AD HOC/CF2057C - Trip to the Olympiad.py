'''
CF2057C - Trip to the Olympiad (https://codeforces.com/contest/2057/problem/C)

Given X and Y, choose a triple of distinct numbers (A, B, C) such that X <= A, B, C <= Y and A XOR B + B XOR C + A XOR C is the maximum.
'''

# TIME COMPLEXITY : O(T)


# 1. TO GET THE INPUT

import sys

test_count = int(sys.stdin.readline())

for test in range(test_count):
    
    min_val, max_val = map(int, sys.stdin.readline().split())
    min_val = bin(min_val)[2:]
    max_val = bin(max_val)[2:]
    min_val = "0" * (31 - len(min_val)) + min_val
    max_val = "0" * (31 - len(max_val)) + max_val
    
    
    # 2. TO FILL EASY DIGITS
    # A bit must not be turned on (or off) in all three numbers.
    
    num = []
    valid = False
    
    for idx in range(31):
        if valid:
            if max_val[idx] == "1":
                if min_val[idx] == "1":
                    num.append("0")
                else:
                    num.append("?")
            else:
                if min_val[idx] == "1":
                    num.append("?")
                else:
                    num.append("1")
        else:
            if max_val[idx] == "1":
                if min_val[idx] == "1":
                    num.append("1")
                else:
                    num.append("?")
                    valid = True
            else:
                if min_val[idx] == "1":
                    num.append("?")
                    valid = True
                else:
                    num.append("0")
    
    
    # 3. TO FILL HARD DIGITS 
    # Let X be the highest bit where the state is different in the largest value and the smallest value.
    # Then, every ? bit higher than X should follow either the largest one or the smallest one.
    # Every ? bit lower than X should follow the other.
    
    key_idx = -1
    clear = True
    
    for idx in range(31):
        if clear:
            if num[idx] == "?":
                clear = False
        else:
            if num[idx] != "?":
                key_idx = idx
                break
    
    if key_idx == -1:
        print(int(max_val, 2), int(min_val, 2), int(min_val, 2) + 1)
    else:
        
        for idx in range(31):
            if num[idx] == "?":
                if num[key_idx] == "1":
                    if idx < key_idx:
                        num[idx] = min_val[idx]
                    else:
                        num[idx] = max_val[idx]
                else:
                    if idx < key_idx:
                        num[idx] = max_val[idx]
                    else:
                        num[idx] = min_val[idx]
        
        num = "".join(num)
        print(int(max_val, 2), int(min_val, 2), int(num, 2))