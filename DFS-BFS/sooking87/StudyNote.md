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

## 실패 코드

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

## 풀이 코드

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

## 코드 설명

1. 입력받기 -> 이중 연결리스트로 입력받기
2. DFS 사용 -> 2번 노드부터 오름차순으로 해당 부모 노드 번호를 출력해라 = 인덱스를 이용해서 한 번에 리스트에 저장(굳이 순서에 상관이 따로 탐색할 필요 없음. 예를 들어서 1 - 6 이라면 6번 째 인덱스에 1을 저장해둠)
