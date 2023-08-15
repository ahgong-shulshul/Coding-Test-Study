n, k = map(int, input().split())

coin = []
for i in range(n):
    coin.append(int(input()))
    
dp = [10001] * (k+1)
dp[0] = 0

for c in coin:
    for i in range(c,k+1):
        if dp[i]>0:
            dp[i] = min(dp[i], dp[i-c]+1)

if dp[k]==10001:
    print(-1)
else:
    print(dp[k])

# 만약 dp[n-c1]이 가장 작다면 "(n-c1)원을 만든 동전의 개수 + c1동전 1개 = n원을 만드는 최소 동전 개수"가 된다.#

