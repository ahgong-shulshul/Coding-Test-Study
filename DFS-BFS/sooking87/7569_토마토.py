# 7569 토마토

# n, m, h 입력
# 익은 토마토를 기준으로 위, 아래, 왼쪽, 오른쪽, 앞, 뒤 여섯 방향에 있는 토마토가 익는다.

import sys
from collections import deque

def count_days(start):
    queue = deque()
    for heig, row, col in start:
        queue.append((heig, row, col))

    # 위, 아래, 앞, 뒤, 왼, 오
    dh = [-1, 1, 0, 0, 0, 0]
    drow = [0, 0, 1, -1, 0, 0]
    dcol = [0, 0, 0, 0, -1, 1]
    
    ansH = 0
    ansY = 0
    ansX = 0
    while queue:
        heig, row, col = queue.popleft()

        for i in range(6):
            nh = heig + dh[i]
            nrow = row + drow[i]
            ncol = col + dcol[i]


            if nh < 0 or nh >= h or nrow < 0 or nrow >= m or ncol < 0 or ncol >= n:
                continue
            if tomatoes[nh][nrow][ncol] == 0:
                tomatoes[nh][nrow][ncol] = tomatoes[heig][row][col] + 1
                queue.append((nh, nrow, ncol))
                ansH = nh
                ansY = nrow
                ansX = ncol
    return ansH, ansY, ansX

def is_ripens(tomatoes):
    for i in range(h):
        for j in range(m):
            for k in range(n):
                if tomatoes[i][j][k] == 0:
                    return False
    return True
input = sys.stdin.readline
n, m, h = map(int, input().split())
tomatoes = []
start = []
for i in range(h):
    floor = []
    for j in range(m):
        temp = [int(i) for i in input().split()]
        floor.append(temp)
        for k in range(n):
            if temp[k] == 1:
                start.append([i, j, k]) # 높이, 행, 열
    tomatoes.append(floor)

ansH, ansY, ansX = count_days(start)
is_all_ripens = is_ripens(tomatoes)
if is_all_ripens:
    print(tomatoes[ansH][ansY][ansX] - 1)
else:
    print(-1)