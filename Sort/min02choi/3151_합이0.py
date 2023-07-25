# 3151 합이 0
# Gold4
# 정렬 알고리즘
# 풀이 날짜: 2023-07-25

n = int(input())
std = [int(m) for m in input().split()]

std.sort()

print(std)
sum = 0
cnt = 0
for i in range(0, len(std) - 2):
    for j in range(i + 1, len(std) - 1):
        for k in range(j + 1, len(std)):
            sum = std[i] + std[j] + std[k]
            if (sum == 0):
                cnt += 1

print(cnt)