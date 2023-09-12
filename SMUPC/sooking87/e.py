# E는 천적 없어 이동 안전 구역
# D는 이동불가 위험 구역
# F는 먹을 수 있음 
# 상하좌우 이동
# 물고기 서식지를 들러 집에 도착할 때 걸리는 최소 시간 출력
# https://www.acmicpc.net/problem/29703

import sys
from collections import deque

def count_sec(start):
    global is_fish
    queue = deque()
    for pos in start:
        queue.append((pos[0], pos[1]))
        visited[pos[0]][pos[1]] = 1
    print('초반', visited)
    dx = [0, 0, -1, 1] # 행을 x축으로
    dy = [-1, 1, 0, 0] # 열을 y축으로

    ansX = 0
    ansY = 0
    while queue:
        x, y = queue.popleft()
        # print('기준 좌표: ', x, y)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if road[nx][ny] == 'D':
                    continue
                visited[nx][ny] = min(visited[nx][ny], visited[x][y] + 1)
                if road[x][y] == 'F':
                    is_fish = True
                if road[nx][ny] == 'F':
                    queue.clear()
                    queue.append((nx, ny))
                elif road[nx][ny] == 'E':
                    # visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))
                elif road[nx][ny] == 'H':
                    # visited[nx][ny] = visited[x][y] + 1
                    ansX = nx
                    ansY = ny
                    break
                # print(visited)
        if road[ansX][ansY] == 'H':
            break
    return ansX, ansY, is_fish


input = sys.stdin.readline
n, m = map(int, input().split())
# n행 m열
road = []
visited = [[0] * m for _ in range(n)]
start = []
is_fish = False
cnt = 0
for i in range(n):
    row = [j for j in input().rstrip()]
    for j in range(m):
        if row[j] == 'S':
            start.append([i, j])
    road.append(row)
# print(road)
# print(visited)
ax, ay, is_fish = count_sec(start)
# print(ax, ay, is_fish)
print(visited)
if is_fish:
    print(visited[ax][ay] - 1)
else:
    print(-1)
