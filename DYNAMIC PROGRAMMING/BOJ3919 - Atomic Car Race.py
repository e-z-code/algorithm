'''
BOJ3919 - Atomic Car Race (https://www.acmicpc.net/problem/3919)

There is a road race with N checkpoints.
A team can change tires at each checkpoint using B seconds.
A car cannot run fast for a while after a tire change.
Of course, a car cannot run fast if its tires wear out.
Determine the best strategy to change tires to minimize the total time.
'''

# TIME COMPLEXITY : O(N^2 * max(A))

import sys
inf = float('inf')


# 1. TO GET THE INPUT

while True:
    
    checkpoint_count = int(sys.stdin.readline())
    if checkpoint_count == 0:
        break
    checkpoints = [0] + list(map(int, sys.stdin.readline().split()))
    
    change_time = float(sys.stdin.readline())
    R, V, E, F = map(float, sys.stdin.readline().split())
    
    
    # 2. TO SOLVE THE PROBLEM
    # DP[i] = Shortest time to reach i-th checkpoint
    
    dp = [inf for checkpoint in range(checkpoint_count + 1)]
    dp[0] = 0
    
    for now_checkpoint in range(checkpoint_count + 1):
        for last_checkpoint in range(now_checkpoint):
            
            time = dp[last_checkpoint]
            if last_checkpoint != 0:
                time += change_time
                
            for dist in range(checkpoints[now_checkpoint] - checkpoints[last_checkpoint]):
                if dist >= R:
                    time += 1 / (V - E * (dist - R))
                else:
                    time += 1 / (V - F * (R - dist))

            dp[now_checkpoint] = min(dp[now_checkpoint], time)
    
    print(dp[-1])