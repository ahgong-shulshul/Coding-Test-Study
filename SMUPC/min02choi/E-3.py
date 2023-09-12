# 물고기 서식지 중 최소한 한 곳을 들러 사냥을 마치고 집으로 돌아가려 한다
# 물고기를 사냥해 최대한 빠르게 펭귄의 집에 도달하는 데 걸리는 시간을 구해보자.

# 1. 물고기 위치 다 저장해서 거기까지의 경로를 다 구함
# 2. 물고기에서 H까지의 경로를 다 구함

# 1과 2의 합이 가장 최소가 되는거리 출력.

# 2차원 리스트 필요

# 미로탐색을 두번 하는 경우임(S->F, F->H)

# 아니면 그냥 다 찾은 다음에 그 안에 F가 있는지 확인 아니 이건 안될듯

from collections import deque
# from sys import stdin

# row, col = list(map(int, stdin.readline().split()))
row, col = map(int, input().split())

# li = []
# li.append(list(map(str, stdin.readline().split())))
# print(li)

graph = []
curr = []   # 현재 위치
home = []   # 도달해야 하는 집 위치
fish = []   # 물고기가 있는 위치

for i in range(row):
    temp = input()
    num_list = []
    for j in range(len(temp)):
        if temp[j] == "S":
            curr.append((i, j))
        if temp[j] == "H":
            home.append((i, j))
        if temp[j] == "F":
            fish.append((i, j))
        
        if temp[j] == "D":
            num_list.append(0)
        else:
            num_list.append(1)
    graph.append(num_list)

# graph_main = copy.deepcopy(graph)

##### 그래프 변환 완료 ########

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, end, gph):
    queue = deque()
    queue.append((x, y))
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
    
            if nx == -1 or nx == row or ny == -1 or ny == col:
                continue

            # print(graph[nx][ny])
            if gph[nx][ny] == 0:
                continue
        
            if gph[nx][ny] == 1:
                queue.append((nx, ny))
                gph[nx][ny] = gph[x][y] + 1
 
    return gph[end[0]][end[1]]
  
curr_fish = []
fish_home = []

for i in range(len(fish)):
    graph1 = [row[:] for row in graph]
    curr_fish.append(bfs(curr[0][0], curr[0][1], fish[i], graph1) - 1)

for i in range(len(fish)):
    graph2 = [row[:] for row in graph]
    fish_home.append(bfs(fish[i][0], fish[i][1], home[0], graph2) - 1)

all_path = []
for i in range(len(curr_fish)):
    if (curr_fish[i] != 0 and fish_home != 0):
        all_path.append(curr_fish[i] + fish_home[i])

all_path.sort()
if len(all_path) == 0:
    print(-1)
else:
    if (all_path[0] == 0):
        print(-1)
    else:
        print(all_path[0])
