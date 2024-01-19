# 14719 빗물
# Gold5
# Implementation 알고리즘
# 풀이 날짜: 2023-07-12

# 굳이 시각화 안해도 되겠는데?


h, w = map(int, input().split())
floor = [int(m) for m in input().split()]

level = max(floor)
total = 0
count = 0

for i in range(0, level + 1):
    idx = 0
    # 첫 번째 인덱스 탐색
    for k in range(w):
        if (floor[k] >= i):
            idx = k
            break
    k = 0
    for k in range(idx + 1, w):
        if (floor[k] < i):  # 빗물 축적
            count += 1
        else:               # 합병
            total += count
            count = 0
    if (k + 1 == w):
        count = 0

print(total)


