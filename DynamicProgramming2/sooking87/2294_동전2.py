# 2294 동전 2

# 가치 합이 k원이 되면서 동전의 개수가 최소가 되도록 하려면 동전은 몇 개가 되는지.

import sys

input = sys.stdin.readline
n, k = map(int, input().split())
value = [int(input()) for i in range(n)]

dp = [100001] * (100000+1)
# print(dp)
for i in value:
    dp[i] = 1

for i in range(min(value)+1, k+1):
    temp = []
    temp.append(dp[i])
    for j in value:
        if (i-j >= 0) and (dp[i-j] <= 100001):
            temp.append(dp[i-j] + 1)
            # print(temp)
    dp[i] = min(temp)
    # print(dp)

print(dp[k] if dp[k] < 100001 else -1)
