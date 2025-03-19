'''
BOJ22526 - Fastest Route (https://www.acmicpc.net/problem/22526)

There are N stages.
If you clear the X-th stage, you earn the X-th armor.
Determine the minimum time required to clear all stages.
'''

# TIME COMPLEXITY : O(pow(2, N) X pow(N, 2))

import sys
inf = float('inf')


# 1. TO GET THE INPUT

while True:
    
    stage_count = int(sys.stdin.readline())
    if stage_count == 0:
        break
    
    clear_time = []
    for stage in range(stage_count):
        stage_time = list(map(int, sys.stdin.readline().split()))
        clear_time.append(stage_time)
    
    
    # 2. BIT-MASKING DP
    # dp[x][i] = Minimum time to clear X when i-th stage is the last stage cleared.
    
    dp = [[inf for last_stage in range(stage_count)] for cleared_stage in range(1 << stage_count)]
    
    for cleared_stage in range(1 << stage_count):
        for last_stage in range(stage_count):
            
            if cleared_stage & (1 << last_stage):
                
                if cleared_stage == (1 << last_stage):
                    dp[cleared_stage][last_stage] = clear_time[last_stage][0]
                else:
                    
                    # Minimum time to clear the last stage
                    min_clear_time = clear_time[last_stage][0]
                    for weapon in range(stage_count):
                        if cleared_stage & (1 << weapon) and weapon != last_stage:
                            min_clear_time = min(min_clear_time, clear_time[last_stage][weapon+1])

                    # Minimum time to clear stages but the last one
                    last_cleared_stage = cleared_stage ^ (1 << last_stage)
                    for second_last_stage in range(stage_count):
                        if last_cleared_stage & (1 << second_last_stage):
                            dp[cleared_stage][last_stage] = min(dp[cleared_stage][last_stage], dp[last_cleared_stage][second_last_stage] + min_clear_time)

    print(min(dp[-1]))