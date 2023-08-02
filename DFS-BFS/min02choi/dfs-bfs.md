## DFS-BFS 알고리즘


### DFS(깊이 우선 탐색)
그래프 탐색의 과정에서 다음 분기로 넘어가기 전에 해당 분기를 완벽하게 탐색하는 방법
* 자료구조 '스택' 사용
* 순환 알고리즘의 형태

~~~python
def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
~~~


### BFS(너비 우선 탐색)
그래프 탐색의 과정에서 특정 노드에서 인접한 노드를 우선으로 탐색하는 방법
* 자료구조 '큐' 사용
* 모든 간선의 비용이 동일한 조건에서 최단거리를 구할 때 주로 사용
* 미로를 빠져나가는 최단거리 문제에서 사용

~~~python
from collections import deque

def bfs (graph, node, visited):
    queue = deque([node])
    visited[node] = True
    
    while queue:
        v = queue.popleft()
        print(v, end = ' ')
        for i in graph[v]:
            if not (visited[i]):
                queue.append(i)
                visited[i] = True
~~~


### 문제에 대한 풀이방법 정리
https://min02choi.github.io/categories/coding-test/baekjoon