# 2156 포도주 시식

# 연속으로 놓여져 있는 포도주 잔에서 최대의 양을 마실 수 있다. 최대의 양을 출력하는 프로그램

import sys

input = sys.stdin.readline
n = int(input())
wine = [0] * 10000
for i in range(n):
    wine[i] = int(input())
# 이것도 부분합처럼 규칙이 있지 않을까?
# 6 10 13 9 8 1
dp = [0] * 10000
dp[0] = wine[0]
dp[1] = wine[0] + wine[1]
# 6 16 23 9
dp[2] = max(wine[2]+wine[0], wine[2]+wine[1], dp[1])
for i in range(3, n):
    dp[i] = max(wine[i]+dp[i-2], wine[i]+wine[i-1]+dp[i-3], dp[i-1])

print(max(dp))
