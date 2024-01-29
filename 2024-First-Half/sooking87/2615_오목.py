# 2615 오목

# 검은 바둑알 1, 흰 바둑알 2, 알이 놓여있지 않는 경우 0
# 출력형식은 검은색 승 1, 흰색 승 2, 승부 결정 X 0
# 검은색 또는 흰색이 이겼을 경우 연속된 다섯 개의 바둑알 중 가장 왼쪽에 있는 바둑알의 가로줄 번호와 세로줄 번호를 차레로 출력

import sys

input = sys.stdin.readline
board = [list(map(int, input().split())) for _ in range(19)]

dx = [1, 1, 0, -1]
dy = [0, 1, 1, 1] # 하, 우하, 우. 우상 확인

def solution():
    for x in range(19):
        for y in range(19):
            if board[x][y]: # 1, 2이면(True)
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    cnt = 1

                    if nx < 0 or ny < 0 or nx >= 19 or ny >= 19:
                        continue
                    while 0 <= nx < 19 and 0 <= ny < 19 and board[x][y] == board[nx][ny]:
                        cnt += 1

                        if cnt == 5:
                            # 육목 확인 1
                            if 0 <= nx+dx[i] < 19 and 0 <= ny+dy[i] < 19 and board[nx][ny] == board[nx+dx[i]][ny+dy[i]]:
                                break
                            # 육목 확인 2
                            if 0 <= x-dx[i] < 19 and 0 <= y-dy[i] < 19 and board[x][y] == board[x-dx[i]][y-dy[i]]:
                                break
                            return board[x][y], x+1, y+1
                        nx += dx[i]
                        ny += dy[i]
    return 0, -1, -1 # 승부가 나기 않을 때

color, x, y = solution()
if not color:
    print(color)
else:
    print(color)
    print(x, y)