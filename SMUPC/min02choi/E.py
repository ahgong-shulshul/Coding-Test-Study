# 물고기 서식지 중 최소한 한 곳을 들러 사냥을 마치고 집으로 돌아가려 한다
# 물고기를 사냥해 최대한 빠르게 펭귄의 집에 도달하는 데 걸리는 시간을 구해보자.

# 1. 물고기 위치 다 저장해서 거기까지의 경로를 다 구함
# 2. 물고기에서 H까지의 경로를 다 구함

# 1과 2의 합이 가장 최소가 되는거리 출력.

# 2차원 리스트 필요

# 미로탐색을 두번 하는 경우임(S->F, F->H)

# 아니면 그냥 다 찾은 다음에 그 안에 F가 있는지 확인 아니 이건 안될듯

from collections import deque


row, col = map(int, input().split())

graph = []
curr = []   # 현재 위치
home = []   # 도달해야 하는 집 위치
fish = []   # 물고기가 있는 위치


for i in range(row):
    temp = input()
    to_num = ""
    for j in range(len(temp)):
        if temp[j] == "S":
            curr.append((i, j))
            # to_num += "1"
        if temp[j] == "H":
            home.append((i, j))
            # to_num += "1"
        if temp[j] == "F":
            fish.append((i, j))
            # to_num += "1"
        
        # 숫자로 변환    
        if temp[j] == "D":
            to_num += "0"
        else:
            to_num += "1"
    graph.append(to_num)

##### 그래프 변환 완료 ########


cur_fish = []
fish_home = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def valid_pt(point):
    # 맵 밖으로 나가면 False
    if point[0] < 0 or point[0] >= row or point[1] < 0 or point[1] >= col:
        return False
    # 첫번째 방문하는 경우만 True
    elif graph[point[0]][point[1]]==1:
        return True
    # 그 외는 False
    else:
        return False

# from collections import deque
def maze_bfs(start, end):
    q = deque()
    q.append(start)
    while q:
        # q에서 현재노드 꺼냄
        cur_pt = q.popleft()
        for i in range(4):
            # 다음 방문할 노드
            next_pt = cur_pt[0] + dx[i], cur_pt[1] + dy[i]
            if valid_pt(next_pt):
                # 현재 노드까지의 거리와 다음 노드의 거리(1)을 합산하여 누적
                graph[next_pt[0]][next_pt[1]]+=graph[cur_pt[0]][cur_pt[1]]
                q.append(next_pt)
    # bfs 종료 후 도착지점 값 출력
    print(graph[row-1][col-1])

maze_bfs(curr, fish)



# def bfs(x, y):
#     queue = deque()
#     queue.append((x, y))

#     for i in range(4):
#         nx, ny = x + dx[i], y + dy[i]



print(graph)
print(fish)
print(home)
