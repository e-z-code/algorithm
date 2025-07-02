'''
BOJ16898 - Item Game (https://www.acmicpc.net/problem/1698)

Initially, there are A distinct boxes and B distinct items.
Every turn, a player must increase the number of either boxes or items.
If the number of ways to put items into boxes is equal to or exceeds N, the player loses.
Determine who will win the game.
'''

# TIME COMPLEXITY : O(sqrt(N) X B)

import sys
sys.setrecursionlimit(10 ** 6)


# 2. A FUNCTION TO SOLVE THE PROBLEM

def game(now_box, now_item, now_turn):
    
    # Even if no one tries to increase the number of items, the game will end.
    if now_box > 100000 and now_item == 1:
        if (number - now_box) % 2 == 0:
            return now_turn
        else:
            return 1 - now_turn
    
    # If no one tries to increase the number of boxes, the game may end in draw.
    if now_box == 1 and pow(2, now_item) >= number:
        dp[now_box][now_item][now_turn] = 2

    # Otherwise...
    if dp[now_box][now_item][now_turn] != -1:
        return dp[now_box][now_item][now_turn]

    # A player always chooses the best option
    if pow(now_box + 1, now_item) >= number:
        if pow(now_box, now_item + 1) >= number:
            dp[now_box][now_item][now_turn] = 1 - now_turn
        else:
            dp[now_box][now_item][now_turn] = game(now_box, now_item + 1, 1 - now_turn)
    else:
        if pow(now_box, now_item + 1) >= number:
            dp[now_box][now_item][now_turn] = game(now_box + 1, now_item, 1 - now_turn)
        else:
            caseA = game(now_box + 1, now_item, 1 - now_turn)
            caseB = game(now_box, now_item + 1, 1 - now_turn)
            if caseA == now_turn or caseB == now_turn:
                dp[now_box][now_item][now_turn] = now_turn
            elif caseA == 2 or caseB == 2:
                dp[now_box][now_item][now_turn] = 2
            else:
                dp[now_box][now_item][now_turn] = 1 - now_turn

    return dp[now_box][now_item][now_turn]


# 1. TO GET THE INPUT

box_count, item_count, number = map(int, sys.stdin.readline().split())


# 3. TO SOLVE THE PROBLEM

dp = [[[-1, -1] for item in range(31)] for box in range(100001)]

winner = game(box_count, item_count, 0)
if winner == 0:
    print("cubelover")
elif winner == 1:
    print("koosaga")
else:
    print("jh05013")