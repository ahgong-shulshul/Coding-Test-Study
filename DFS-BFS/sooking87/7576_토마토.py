# 7675 토마토

# 익은 토마토와 인접해 있으면 위, 아래, 오른쪽, 왼쪽이 익는다
# 1: 익은 토마토, 0: 익지 않은 토마토, -1: 토마토가 없음

# 1이 있는 위치 찾기 -> 1이 없으면 모든 토마토가 익을 수 없음
# -1이 있더라도 모두 익을 수는 있음
# BFS, DFS를 어케 사용? -> 미로 탐색 참고

import sys
# 먼저 들어간 좌표에 대해서 주변 토마토가 익어야되므로 큐 사용
from collections import deque

def count_days(start):
    queue = deque()
    for pos in start:
        queue.append((pos[0], pos[1]))

    dx = [0, 0, -1, 1] # 행을 x축으로
    dy = [-1, 1, 0, 0] # 열을 y축으로

    ansX = 0
    ansY = 0
    while queue:
        x, y = queue.popleft()
        # print(x, y)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # print(nx, ny)
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if tomatoes[nx][ny] == 0:
                tomatoes[nx][ny] = tomatoes[x][y] + 1
                queue.append((nx, ny))
                ansX = nx
                ansY = ny
        # print(tomatoes)
    return ansX, ansY

def is_ripens(tomatoes):
    for i in range(m):
        for j in range(n):
            if tomatoes[i][j] == 0:
                return False
    return True

input = sys.stdin.readline
n, m = map(int, input().split())
tomatoes = []
start = []

for j in range(m):
    row = [int(i) for i in input().split()]
    for i in range(n):
        if row[i] == 1:
            start.append([j, i])
    tomatoes.append(row)

x, y = count_days(start)
is_all_ripens = is_ripens(tomatoes)
if is_all_ripens:
    print(tomatoes[x][y] - 1)
else:
    print(-1)

