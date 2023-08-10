# 1890 점프

# N×N 게임판: 0은 종착점, 항상 현재 칸에 적혀있는 수만큼 오른쪽이나 아래로 가야된다. -> (0, 0) 위치에서 규칙에 맞게 이동할 수 있는 경로의 개수

import sys

input = sys.stdin.readline
n = int(input())
board = [[int(i) for i in input().split()] for _ in range(n)]
cnt = [[0 for i in range(n)] for _ in range(n)]
cnt[0][0] = 1  # 초기 값

for col in range(n):
    for row in range(n):
        if col == n - 1 and row == n - 1:
            print(cnt[col][row])
            break
        # 오른쪽으로 이동
        if row + board[col][row] < n:
            cnt[col][row + board[col][row]] += cnt[col][row]

        # 아래쪽으로 이동
        if col + board[col][row] < n:
            cnt[col + board[col][row]][row] += cnt[col][row]
