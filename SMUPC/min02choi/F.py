n, t = map(int, input().split())

data = []
data.append([0, 0])


for i in range(n):
    data.append([int(m) for m in input().split()])


dp = [0] * (t + 2)
for i in range(t, 0, -1):
    if (i + data[i][0] > t + 1):
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(data[i][1] + dp[i + data[i][0]], dp[i + 1])

print(dp[1])