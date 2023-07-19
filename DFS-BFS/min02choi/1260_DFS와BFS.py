# 1260 DFS와 BFS
# Silver2
# BFS(깊이 우선 탐색), DFS(너비 우선 탐색) 알고리즘
# 풀이 날짜: 2023-07-19


from collections import deque

def bfs(graph, v, visited):
    visited[v] = True
    print(v, end=" ")
    for i in graph[v]:
        if (visited[i] == False):
            bfs(graph, i, visited)


def dfs(graph, v, visited):
    visited[v] = True
    queue = deque([v])

    while queue:
        node = queue.popleft()
        print(node, end=" ")
        for i in graph[node]:
            if (visited[i] == False):
                queue.append(i)
                visited[i] = True
    

n, m, v = map(int, input().split())
graph = [[] for i in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n):
    graph[i].sort()

visited = [False] * (n + 1)
bfs(graph, v, visited)
print()

visited = [False] * (n + 1)
dfs(graph, v, visited)