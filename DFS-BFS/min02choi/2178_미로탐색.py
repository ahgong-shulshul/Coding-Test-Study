# 2178 미로 탐색
# Silver1
# BFS(너비 우선 탐색) 알고리즘
# 풀이 날짜: 2023-07-20


# 풀이 방법 -> BFS 사용
# 각 사방팔방마다 1이 있는 곳으로 전진
# board를 넘어가는지 확인
# 방문한 자리인지 확인
# 해당 위치까지의 거리를 graph에 저장해가면서 진행
# 탐색 완료 후 마지막 자리에 있는 수 출력

from collections import deque


n, m = map(int, input().split())
graph = []
for i in range(n):
    temp = list(map(int, input()))
    graph.append(temp)

visited = [[False] * m for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

path = deque()      # iterable 에러 방지 위해 우선 선언
path.append((0, 0))
visited[0][0] = True

while (path):
    x, y = path.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if (0 <= nx < m and 0 <= ny < n):
            if (graph[ny][nx] == 1 and visited[ny][nx] == False):
                graph[ny][nx] = graph[y][x] + 1
                visited[ny][nx] = True
                path.append((nx, ny))

""" 확인을 위한 그래프 출력
for i in range(n):
    for j in range(m):
        print(graph[i][j], end=" ")
    print()
"""

print(graph[n][m])
