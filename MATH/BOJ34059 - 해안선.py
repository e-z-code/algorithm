import sys
MOD = pow(10, 9) + 7


# 2. A FUNCTION FOR COMBINATION

def combination(N, K):
    
    return ((factorial[N] % MOD) * pow(factorial[N-K] * factorial[K], MOD-2, MOD)) % MOD


# 1. TO GET THE INPUT

node_count = int(sys.stdin.readline())
nodeA, nodeB = map(int, sys.stdin.readline().split())
if nodeA > nodeB:
    nodeA, nodeB = nodeB, nodeA


# 3. TO SOLVE THE PROBLEM
# The number of non-crossing hamilton cycles given a starting point equals pow(2, N-2).

factorial = [1]
for num in range(1, 1000001):
    factorial.append(factorial[-1] * num % MOD)

left_count = node_count - nodeB
right_count = nodeA - 2

if nodeB - nodeA == 1:
    # Think of (nodeA, nodeB) as a single node.
    ans = (pow(2, node_count - 3, MOD) + combination(left_count + right_count, left_count)) % MOD
else:
    other_count = nodeB - nodeA
    ans = ((combination(left_count + right_count, left_count) * 2 % MOD) * pow(2, other_count - 2, MOD)) % MOD

print(ans)
    