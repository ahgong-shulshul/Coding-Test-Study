# M행 N열의 직사각형 -> 모두 가로로 이어 앉는 경우의 수

import sys

input = sys.stdin.readline
# n행, m열, k명
n, m, k = map(int, input().split())
seat = []
for _ in range(n):
    temp = input().rstrip()
    seat.append(temp)
# print('0'*k)
cnt = 0

for i in range(len(seat)):
    for j in range(m - k + 1):
        # print(seat[i][j:j+k])
        if seat[i][j:j+k] == '0'*k:
            cnt += 1

print(cnt)
