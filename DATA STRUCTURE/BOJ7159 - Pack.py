'''
BOJ7159 - Pack (https://www.acmicpc.net/problem/7159)

There is a pack of N cards. 
In each of M turn, you take the upper K cards and turn them upside down.
Determine the state and location of each card after the moves.
'''

# TIME COMPLEXITY : O(NM)

import sys
from collections import deque


# 1. TO GET THE INPUT

card_count, move_count = map(int, sys.stdin.readline().split())


# 2. TO SIMULATE MOVES

cards = [card_count - idx for idx in range(card_count)]
queue = deque([])

for move in range(move_count):
    
    cards_to_move = int(sys.stdin.readline())
    while cards_to_move != 0:
        queue.append(cards.pop())
        cards_to_move -= 1
    while queue:
        cards.append(-queue.popleft())


# 3. TO STORE ANSWERS

ans = [0 for card in range(card_count + 1)]

for idx in range(card_count):
    
    card = cards[idx]
    if card > 0:
        ans[card] = "+{}".format(card_count - idx)
    else:
        ans[abs(card)] = str(idx - card_count)
        

# 4. TO ANSWER QUERIES

query_count = int(sys.stdin.readline())

for query in range(query_count):
    
    card = int(sys.stdin.readline())
    print(ans[card])