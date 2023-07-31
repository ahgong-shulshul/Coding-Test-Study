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
count = 1
while end >= 1:
    end //= 2
    count += 1
    # print(end)
    if n == count:
        break
# print('----------')
if end == 1:
    print('YES')
else:
    print('NO')
