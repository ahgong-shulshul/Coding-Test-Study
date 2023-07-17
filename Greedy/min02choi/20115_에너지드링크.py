# 20115 에너지 드링크
# Greedy 알고리즘
# 풀이 날짜: 2023-07-04

# 알고리즘 무시 나의 방식... 아니면 이게 그리디 알고리즘인가?
# 에너지 드링크 하나를 제외하면 나머지는 다 절반이 줄어든다. 즉, 가장 큰 용량을 가진 에너지 드링크에 나머지 에너지 드링크를 집어넣는다.

n = int(input())
drinks = [float(m) for m in input().split()]

drinks.sort(reverse=True)

total = 0
total += drinks[0]
for i in range(1, n):
    total += drinks[i] / 2

print(total)