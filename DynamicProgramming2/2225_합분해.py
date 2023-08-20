# 2225 합분해
# Gold5
# 동적 계획법
# 풀이 날짜: 2023-08-15

# 1을 만들 수 있는 경우의 수
# 2를 만들 수 있는 경우의 수
# 3을 만들 수 있는 경우의 수
# 위의 경우들을 모두 계산하고 4를 만들수 있는 수: 1+3, 3+1, 2+2

# k개의 숫자를 가지고 n을 만들 수 있는 경우의 수: dp[k][n]


n, k = map(int, input().split())
dp = [[0 for _ in range(201)] for _ in range(201)]

for i in range(201):
    dp[1][i] = 1
    dp[i][0] = 1

for i in range(1, k + 1):
    for j in range(1, n + 1):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

print(dp[k][n] % 1000000000)
