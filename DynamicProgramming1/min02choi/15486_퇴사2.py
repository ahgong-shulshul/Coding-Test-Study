# 15486 퇴사2
# Gold5
# 동적 계획법
# 풀이 날짜: 2023-08-11


import sys 


input = sys.stdin.readline

n = int(input())
data = []
data.append([0, 0])
for i in range(n):
    data.append([int(m) for m in input().split()])

dp = [0] * (n + 2)
for i in range(n, 0, -1):
    if (i + data[i][0] > n + 1):
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(data[i][1] + dp[i + data[i][0]], dp[i + 1])

print(dp[1])
