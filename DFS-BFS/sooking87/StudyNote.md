# DFS & BFS

📌 [[Daily PS] 파이썬으로 구현하는 BFS와 DFS](https://cyc1am3n.github.io/2019/04/26/bfs_dfs_with_python.html)

## DFS(Depth First Search, 깊이 우선 탐색)

![gif](https://upload.wikimedia.org/wikipedia/commons/7/7f/Depth-First-Search.gif) <br>

스택을 사용해서 구현 가능 <br>
파이썬에서 스택은 리스트를 사용해서 `append` 와 `pop` 을 사용

```python
def DFS(graph, root):
    visited = []
    stack = [root]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            # 방문 했던 노드는 제외하고 스택에 추가
            stack += graph[n] - set(visited)
    return ''.join(str(i) for i in visited)
```

## BFS(Breadth First Search, 너비 우선 탐색)

![gif](https://upload.wikimedia.org/wikipedia/commons/5/5d/Breadth-First-Search-Algorithm.gif) <br>

이 알고리즘의 핵심은 **큐** 자료구조를 사용하는 것이다. <br>
노드를 방문하면서 인접한 노드 중 방문하지 않았던 노드의 정보만 큐에 넣어서 먼저 큐에 들어있던 노드부터 방문 <br>

파이썬으로 큐를 구현하는 방법으로는 <br>
`list.append` , `list.pop(0)` -> 비효율적인 코드 <br>
`from collections import deque` :: `queue.append` , `queue.popleft()` -> 사용

```python
def BFS(graph, root):
    visited = []
    queue = deque([root])

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            queue += graph[n] - set(visited)

    return visited
```

## 백준 11725 트리의 부모 찾기

📌 [백준 11725 문제 링크](https://www.acmicpc.net/problem/11725) <br>

### 실패 코드

```python
# 11725 트리의 부모 찾기

# 각 노드의 부모를 구하는 프로그램 작성하기

import sys


def traversal(tree, item):
    for key, value in tree.items():
        for i in range(len(value)):
            if item == value[i]:
                return key


input = sys.stdin.readline

n = int(input())
node = [1]
tree = {}
for _ in range(n - 1):
    n1, n2 = map(int, input().split())
    if n1 in node:
        prnt = n1
        chld = n2
    else:
        prnt = n2
        chld = n1
    node.append(chld)
    if prnt in tree:
        tree[prnt].append(chld)
    else:
        tree[prnt] = [chld]

for i in range(2, n + 1):
    ans = traversal(tree, i)
    print(ans)
```

딕셔너리(tree) -> 부모: 자식 리스트 순으로 입력받음 <br>

traversal 함수를 통해서 2번 노드부터 순차적으로 해당 부모 노드를 출력하고자 함 -> `시간 초과` <br>

내 생각에는 traversal 함수가 시간 초과 원인인듯 <br>

아 그리고 얘는 DFS-BFS 문제이므로,,,,,, 써야겠지?

### 풀이 코드

```python
# 11725 트리의 부모 찾기

# 각 노드의 부모를 구하는 프로그램 작성하기

import sys


def traversal(tree, node, visited):
    visited[node] = 1
    stack = [node]
    while stack:
        n = stack.pop()
        for i in tree[n]:
            if not visited[i]:
                stack.append(i)
                visited[i] = 1
                # 인덱스를 이용해서 해당 부모 노드를 리스트에 저장
                parent[i] = n


input = sys.stdin.readline

n = int(input())

# 입력값 -> 이중 리스트로 받음
tree = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
parent = [0] * (n + 1)
for _ in range(n - 1):
    n1, n2 = map(int, input().split())
    tree[n1].append(n2)
    tree[n2].append(n1)

# 2번 노드부터 순서대로 출력한다 == 결국 탐색하면서 해당 인덱스의 부모 노드 번호를 넣어두면 됨.
traversal(tree, 1, visited)
for i in range(2, n + 1):
    print(parent[i])

```

### 코드 설명

1. 입력받기 -> 이중 연결리스트로 입력받기
2. DFS 사용 -> 2번 노드부터 오름차순으로 해당 부모 노드 번호를 출력해라 = 인덱스를 이용해서 한 번에 리스트에 저장(굳이 순서에 상관이 따로 탐색할 필요 없음. 예를 들어서 1 - 6 이라면 6번 째 인덱스에 1을 저장해둠)


## 백준 7576 토마토

📌 [백준 7576 문제 링크](https://www.acmicpc.net/problem/7576) <br>

익은 토마토와 인접해 있으면 위, 아래, 오른쪽, 왼쪽이 익는다. <br>
1: 익은 토마토, 0: 익지 않은 토마토, -1: 토마토가 없음 <br>

토마토가 다 익는 최소 일수를 출력하는 프로그램

### 풀이 코드

```python
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
```

트리 형태의 경우는 `visited` 를 통해서 방문 여부를 파악했지만, 이중 리스트의 경우는 인덱스를 통해서, 또는 해당 인덱스의 값을 통해서 방문 여부를 파악한다. <br>
누가봐도 트리를 사용한 문제의 경우는 해당 값(노드의 value)를 출력해야되는 경우가 많으므로 visited를 통해서 파악했지만, 이중 리스트의 경우는 해당 값을 수정해가면서 방문 여부를 알 수 있기 때문에 visited가 굳이 필요없었다. <br>
경우에 따라서 이중 리스트임에도 visited가 필요할 수도 있겠지? <br>

그리고 토마토가 익은 순대로 주변 토마토가 익음을 수정해주어야 하므로 큐를 사용 -> BFS 사용

### 코드 설명

익은 토마토 기준으로 위, 아래, 왼쪽, 오른쪽이 0이면 익어야되므로 tomatoes[x][y] 기준으로 1을 더해준다. 1로 넣어도되지만 최종적으로 구해야하는 값이 익은 일수이므로 count 대신 리스트 안의 값으로 활용했다.
