# 1890 점프

# N×N 게임판: 0은 종착점, 항상 현재 칸에 적혀있는 수만큼 오른쪽이나 아래로 가야된다. -> (0, 0) 위치에서 규칙에 맞게 이동할 수 있는 경로의 개수

import sys


def dp(cnt, col, row):
    print('n:', n)
    if row >= 0 and row < n:  # 오른쪽으로 이동 = 열 이동
        cnt[col][board[col][row]] += 1
        row += board[col][row]
        print('오른쪽으로 이동', cnt, col, row)
        return dp(cnt, col, row)

    if col >= 0 and col < n:  # 아래로 이동 = 행 이동
        cnt[board[col][row]][row] += 1
        col += board[col][row]
        print('아래쪽으로 이동', cnt, col, row)
        return dp(cnt, col, row)

    if board[col][row] == 0:
        cnt[col][row] += 1

        print(cnt, col, row)


input = sys.stdin.readline
n = int(input())
board = [[int(i) for i in input().split()] for _ in range(n)]
cnt = [[0 for i in range(n)] for _ in range(n)]
col = 0
row = 0
dp(cnt, col, row)
