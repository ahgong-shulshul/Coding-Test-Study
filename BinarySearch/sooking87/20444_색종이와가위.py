# 20444 색종이와 가위

# n번의 가위질로 k개의 색종이 조각을 만들 수 있다면 YES, 아니라면 NO를 출력

import sys

input = sys.stdin.readline
n, k = map(int, input().split())
# 1번 자름 -> 2개
# 2번 자름 -> 4개
# 3번 자름 -> 6개
# 4번 자름 -> 9개 / 8개
start = 1
end = k
cnt = 0

while start <= end:
    mid = (start + end) // 2  # 이 문제에서는 mid가 어떤 거를 의미할까? ->
    temp = cnt + mid
    if temp >= k:
        start = mid + 1
    else:
        end = mid - 1
    cnt += 1
    print(mid)
if cnt == n:
    print('YES')
else:
    print('NO')
