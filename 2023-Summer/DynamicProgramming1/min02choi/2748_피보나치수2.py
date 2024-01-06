# 2748 피보나치 수 2
# Bronze1
# 동적 계획법
# 풀이 날짜: 2023-08-07

# 상향식 방법

n = int(input())

num = [0, 1]
for i in range(1, n):
    num.append(num[i - 1] + num[i])
print(num[n])