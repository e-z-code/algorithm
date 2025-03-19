'''
BOJ17258 - Popularity Overflow (https://www.acmicpc.net/problem/17258)

Your friend Wookje invited M people to his birthday party.
However, he will leave the room if there are less than T people.
You want Wookje to stay in the room as long as possible by inviting K friends.
Your friends will leave and never return if there are more than T people in the room.
Determine the longest time Wookje will stay.
'''

# TIME COMPLEXITY : O(NK^2)

import sys


# 1. TO GET THE INPUT

party_length, invited_count, friend_count, min_count = map(int, sys.stdin.readline().split())


# 2. TO CHECK HOW MANY PEOPLE ARE AT THE PARTY AT EACH MINUTE - IMOS

present = [0 for time in range(party_length + 1)]

for invited_person in range(invited_count):
    start, end = map(int, sys.stdin.readline().split())
    start -= 1
    end -= 1
    present[start] += 1
    present[end] -= 1

for time in range(party_length):
    present[time+1] += present[time]


# 3. TO CHECK HOW LONGER WOOKJE CAN STAY WHEN FRIENDS COME
# options[i][j] = How longer Wookje can stay when j friends come at i-th interval

options = []
option = [0 for added_friend in range(friend_count + 1)]

for time in range(party_length + 1):
    if min_count <= present[time] or time == party_length:
        if sum(option) != 0:
            for added_friend in range(friend_count):
                option[added_friend+1] += option[added_friend]
            options.append(option)
        option = [0 for added_friend in range(friend_count + 1)]
    else:
        added_friend = min_count - present[time]
        if 0 < added_friend <= friend_count:
            option[added_friend] += 1


# 4. TO SOLVE THE PROBLEM - DYNAMIC PROGRAMMING
# DP[i][j] = Maximum number of time Wookje can stay more when j friends come considering first i intervals.

dp = [[0 for added_friend in range(friend_count + 1)] for option_idx in range(len(options))]

for option_idx in range(len(options)):
    for added_friend in range(friend_count + 1):
        
        if option_idx == 0:
            dp[option_idx][added_friend] = options[option_idx][added_friend]
        else:
            for newly_added_friend in range(friend_count + 1):
                if 0 <= added_friend - newly_added_friend:
                    dp[option_idx][added_friend] = max(dp[option_idx][added_friend], dp[option_idx-1][added_friend-newly_added_friend] + options[option_idx][newly_added_friend])

ans = dp[-1][-1]
for time in range(party_length):
    if present[time] >= min_count:
        ans += 1
print(ans)