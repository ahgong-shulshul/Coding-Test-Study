# 9655 돌 게임
# Silver5
# 동적 계획법
# 풀이 날짜: 2023-08-17


n = int(input())

if (n % 2 == 0):
    print("CY")
else:
    print("SK")


# 굳이 동적 계획법으로 풀자면..
# 아니 이거 동적계획법으로 어케 풂?
"""
n = int(input())

person = "S"
dp = [0] * (n + 1)
dp[1] = "S"
dp[2] = "C"
dp[3] = "S"
for i in range(4, n + 1):
    if (dp[i - 1] == "S"):
        dp[i] = "C"
    else:
        dp[i] = "S"

print(dp[n])
"""