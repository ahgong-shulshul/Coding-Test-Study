# 10844 쉬운 계단 수

# 옆 계단이 1차이가 나는 계단이 쉬운 계단이다. 길이가 n인 계단 수가 총 몇개 있는지, 1로 시작하는 계단수

import sys

input = sys.stdin.readline
n = int(input())  # n 자리수

# dp 테이블 초기화,,
dp = [[0] * 10 for _ in range(n + 1)]

# 1의 자릿수의 경우의 수 초기화
for i in range(1, 10):
    dp[1][i] = 1

# 나머지 자릿수의 경우의 수 탐색
for i in range(2, n + 1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][1]
        elif 1 <= j <= 8:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
        else:
            dp[i][j] = dp[i-1][8]
print(sum(dp[n]) % 1000000000)
