# 9055 1, 2, 3 더하기
# Silver3
# 동적 계획법
# 풀이 날짜: 2023-08-20


dp = [0] * 11
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, 11):
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

t = int(input())
for i in range(t):
    print(dp[int(input())])