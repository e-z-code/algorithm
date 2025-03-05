'''
BOJ5769 - Make a Guess (https://www.acmicpc.net/problem/5769)

Given guesses and results of "Bulls and Cows", determine the possible answer.
'''

# TIME COMPLEXITY : O(N X pow(K, L))

import sys
from itertools import product


# 1. TO GET THE INPUT

while True:
    
    guess_count, password_length, char_count = map(int, sys.stdin.readline().split())
    if guess_count == 0 and password_length == 0 and char_count == 0:
        break

    chars = list(sys.stdin.readline().strip())

    guesses = []
    for guess in range(guess_count):
        guessed_password, strike, out = sys.stdin.readline().strip().split()
        strike = int(strike)
        out = int(out)
        guesses.append((guessed_password, strike, out))
    
    
    # 2. BRUTE-FORCE
    
    ans = [set() for idx in range(password_length)]
    
    for password in product(chars, repeat=password_length):
        
        valid = True
        
        for guess in guesses:
            
            guessed_password, strike, out = guess
            
            now_strike = 0
            now_out = 0
            
            password_left = {}
            guess_left = {}
            
            for idx in range(password_length):
                if password[idx] == guessed_password[idx]:
                    now_strike += 1
                else:
                    password_left[password[idx]] = password_left.get(password[idx], 0) + 1
                    guess_left[guessed_password[idx]] = guess_left.get(guessed_password[idx], 0) + 1
            
            for char in chars:
                now_out += min(password_left.get(char, 0), guess_left.get(char, 0))
            
            if strike != now_strike or out != now_out:
                valid = False
                break
        
        if valid:
            for idx in range(password_length):
                ans[idx].add(password[idx])
    
    
    # 3. TO SOLVE THE PROBLEM
    
    for idx in range(password_length):
        if len(ans[idx]) == 1:
            ans[idx] = list(ans[idx])[0]
        else:
            ans[idx] = "?"
    
    print("".join(ans))