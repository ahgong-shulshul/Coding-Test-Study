# 17626 Four Squares
# Silver4
# 동적 계획법
# 풀이 날짜: 2023-08-16


n = int(input())
dp = [0] * (n + 2)

for i in range(1, n + 1):
    dp[i] = dp[i - 1] + 1
    j = 1
    while (j * j <= i):
        dp[i] = min(dp[i], dp[i - j * j] + 1)
        j += 1

print(dp[n])