# 1654 랜선 자르기

# k개의 랜선을 가지고 있는데, N개의 같은 길이의 랜선을 만들고 싶다.

import sys

input = sys.stdin.readline
k, n = map(int, input().split())
lines = []
for _ in range(k):
    lines.append(int(input()))

start = 1
end = max(lines)

while start <= end:
    mid = (start + end) // 2  # 최대 길이가 mid일 때
    line_cnt = 0
    # 개수가 count
    for i in lines:
        line_cnt += i // mid

    if line_cnt >= n:
        start = mid + 1
    else:
        end = mid - 1
print(end)
