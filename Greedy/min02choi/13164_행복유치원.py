# 13164 행복 유치원
# Gold5
# Greedy 알고리즘
# 풀이 날짜: 2023-07-07

# 풀이 전략
# 각 그룹 별 간격 체크 -> 가장 작은 간격을 가진 그룹부터 그룹화
# -> 간격을 오름차순으로 정렬 후, 특정 수(num-group) 까지 더하기


import sys

input = sys.stdin.readline

num, group = map(int, input().split())
member = list(map(int, input().split()))

dist = [member[i + 1] - member[i] for i in range(num - 1)]
dist.sort()
print(sum(dist[:num-group]))


"""
import sys

input = sys.stdin.readline

num, group = map(int, input().split())
# member = [int(m) for m in input().split()]
member = list(map(int, input().split()))

dist = [member[i + 1] - member[i] for i in range(num - 1)]

cnt = 0
n = num - group
for _ in range(n):
    min_idx = dist.index(min(dist))
    if (min_idx == 0 and len(dist) != 1):
        dist[min_idx + 1] += dist[min_idx]
    elif (min_idx != 0 and min_idx == len(dist) - 1):
        dist[min_idx - 1] += dist[min_idx]
    else:
        dist[min_idx + 1] += dist[min_idx]
        dist[min_idx - 1] += dist[min_idx]

    cnt += dist[min_idx]
    del dist[min_idx]

print(cnt)
"""