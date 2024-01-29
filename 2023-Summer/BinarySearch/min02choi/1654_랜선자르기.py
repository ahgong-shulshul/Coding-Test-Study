# 1654 랜선 자르기
# Silver2
# 이진탐색
# 풀이 날짜: 2023-08-05


# 더 많이 나왔다? -> mid를 증가해도 됨
# 더 적게 나왔다? -> mid를 감소해야 함


k, n = map(int, input().split())
line = []
for i in range(k):
    line.append(int(input()))

low = 1
high = max(line)

while (low <= high):
    mid = (low + high) // 2
    total = 0
    for i in range(k):
        total += line[i] // mid
    
    if (total >= n):
        low = mid + 1
    else:
        high = mid - 1

print(high)