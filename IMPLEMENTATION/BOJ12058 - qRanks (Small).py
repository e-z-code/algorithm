'''
BOJ12058 - qRanks (Small) (https://www.acmicpc.net/problem/12058)

In each competition, top P players get points of (RANK POINT) x (COMPETITION WEIGHT).
When calculating seasonal ranking, only the M highest scores will count for each player.
Determine the rank of all athletes who appeared in the competitions at least once.
'''

# TIME COMPLEXITY : O(TNP(N log N + M))

import sys


# 1. TO GET THE INPUT

test_count = int(sys.stdin.readline())

for test in range(1, test_count + 1):
    
    top_rank = int(sys.stdin.readline())
    score = list(map(int, sys.stdin.readline().split()))
    
    
    # 2. TO RECORD ALL POINTS EARNED BY EACH PLAYER
    
    record = {}
    
    competition_count = int(sys.stdin.readline())
    for competition in range(competition_count):
        
        info = list(sys.stdin.readline().strip().split())
        weight = int(info[0])
        
        for rank in range(1, len(info)):
            player = info[rank]
            point = score[rank-1] * weight
            if player in record:
                record[player].append(point)
            else:
                record[player] = [point]
    
    
    # 3. TO CALCULATE VALID POINTS
    
    ranking = []
    max_game = int(sys.stdin.readline())
    
    for player in record:
        
        point = 0
        sorted_record = sorted(record[player], reverse=True)
        
        for idx in range(min(len(sorted_record), max_game)):
            point += sorted_record[idx]
        
        ranking.append((-point, player)) # For ordering

    ranking.sort()
    

    # 4. TO RANK ALL PLAYERS
    
    print("Case #{}:".format(test))
    
    idx = 0
    rank = 0
    while True:
        if idx >= len(ranking):
            break
        point, player = ranking[idx]
        if idx == 0 or ranking[idx][0] != ranking[idx-1][0]:
            rank = idx + 1
        print("{}: {}".format(rank, player))
        idx += 1