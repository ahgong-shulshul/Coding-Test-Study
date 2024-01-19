# 11053 가장 긴 증가하는 부분 수열
# Silver2
# 동적 계획법
# 풀이 날짜: 2023-08-09


# 100, 20, 10, 20, 15, 20, 30
#   1,  1,  1,  2,  2,  3,  4
# 현재 수에 도달: 이전 수 중에서 현재 수보다 작은 수 중에서 가장 큰 길이를 가진 수 + 1

n = int(input())
a = [int(m) for m in input().split()]

cnt = [0] * n
cnt[0] = 1      # 첫째 수까지는 1개

for i in range(1, n):
    temp = [0] * n

    for j in range(0, i):
        if (a[j] < a[i]):
            temp[j] = cnt[j]
    cnt[i] = max(temp) + 1

print(max(cnt))