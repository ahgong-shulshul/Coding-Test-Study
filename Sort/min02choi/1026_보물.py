# 1026 보물
# Silver4
# 정렬 알고리즘
# 풀이 날짜: 2023-07-26


n = int(input())
a = [int(m) for m in input().split()]
b = [int(m) for m in input().split()]

a.sort(reverse=True)
b.sort()

sum = 0
for i in range(n):
    sum += a[i] * b[i]
print(sum)
