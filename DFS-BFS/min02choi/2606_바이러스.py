# 2606 바이러스
# Silver3
# 그래프 탐색 알고리즘?
# 풀이 날짜: 2023-07-17

def dfs(graph, v, visited):
    global cnt
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            cnt += 1
            dfs(graph, i, visited)

n = int(input())
k = int(input())

visited = [False] * (n + 1)
com = [[] for i in range(n + 1)]
cnt = 0

for i in range(k):
    a, b = map(int, input().split())
    com[a].append(b)
    com[b].append(b)

print(com)

print(dfs(com, 1, visited))
print(cnt)





"""
n = int(input())
k = int(input())

n, k

com = [False] * n
for i in range(k):
    a, b = map(int, input().split())
    if (a == 1 or b == 1):
        com[a - 1] = True
        com[b - 1] = True
    if com[a - 1] == True:
        com[b - 1] =True
    if com[b- 1] == True:
        com[a - 1] =True
cnt = 0
for i in range(1, n):
    if (com[i] == True):
        cnt += 1

print(cnt)
"""