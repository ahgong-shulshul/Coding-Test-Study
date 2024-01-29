# 2293 동전 1

# n가지 종류의 동전 -> 가치의 합이 k원이 되도록하고 싶다. 그 경우의 수는?

import sys

input = sys.stdin.readline
n, k = map(int, input().split())
value = [int(input()) for i in range(n)]

dp = [0] * (k+1)
dp[0] = 1
# dp[k] 가 답이 될 수 있도록
for i in value:
    for j in range(i, k+1):
        if j-i >= 0:
            dp[j] += dp[j-i]
        # print(dp)
print(dp[k])