'''
BOJ12494 - Space Emergency (Large) (https://www.acmicpc.net/problem/12494)

You want to travel from star 0 to star N in increasing numerical order.
You normally travel at a speed of 0.5LY per hour.
It is possible to order engineers to build up L boosters at different stars.
Building a booster takes X hours.
If a booster is completed, you can travel at a speed of 1LY per hour for that route.
'''

# TIME COMPLEXITY : O(TN log N)
# BOJ12493 is the easier version of this problem. It can be solved by the same code.

import sys
inf = float('inf')


# 1. TO GET THE INPUT

test_count = int(sys.stdin.readline())

for test in range(1, test_count + 1):
    
    info = list(map(int, sys.stdin.readline().split()))
    boost_count, boost_time, star_count, loop_count, loop = info[0], info[1], info[2], info[3], info[4:]
    
    dist = []
    idx = 0
    while len(dist) < star_count:
        dist.append(loop[idx])
        idx = (idx + 1) % loop_count


    # 2. TO GET DISTANCES THAT CAN BE SAVED
    
    savable = []
    now_time = 0
    
    for idx in range(len(dist)):
        if boost_time <= now_time:
            savable.append(dist[idx])
            now_time += dist[idx]
        elif boost_time <= now_time + dist[idx] * 2:
            savable.append(dist[idx] - (boost_time - now_time) // 2)
            now_time += dist[idx] + (boost_time - now_time) // 2
        else:
            now_time += dist[idx] * 2
    
    savable.sort()
    
    
    # 3. TO SOLVE THE PROBLEM
    
    ans = sum(dist) * 2
    for idx in range(1, boost_count + 1):
        if len(savable) < idx:
            break
        ans -= savable[-idx]
    print("Case #{}: {}".format(test, ans))