# 벌금 최소 금액
import sys

input = sys.stdin.readline
n, t = map(int, input().split())
dp = [0] * (t+1)
total = 0
for _ in range(n):
    k, s = map(int, input().split())
    total += s
    for i in range(t, -1, -1):
        if i >= k:
            dp[i] = max(dp[i], dp[i-k] + s)
print(total - dp[t])