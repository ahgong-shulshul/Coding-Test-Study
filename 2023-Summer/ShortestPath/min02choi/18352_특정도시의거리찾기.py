# 18352 특정 도시의 거리 찾기
# Silver2
# String
# 풀이 날짜: 2023-08-30

INF = int(1e9)

def get_smallest_node():
    min_val = INF
    index = 0
    for i in range(1, n + 1):
        if dist[i] < min_val and not visited[i]:
            min_val = dist[i]
            index = i
    return index


def dijkstra(start):
    dist[start] = 0
    visited[start] = True

    for i in path[start]:
        dist[i] = 1

    for i in range(n - 1):
        now = get_smallest_node()
        visited[now] = True
        for j in path[now]:
            cost = dist[now] + 1
            if cost < dist[j]:
                dist[j] = cost


n, m, k, x = map(int, input().split())
path = [[] for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    path[a].append(b)

visited = [False] * (n + 1)
dist = [INF] * (n + 1)


dijkstra(x)
ans = []
for i in range(1, n + 1):
    if dist[i] == k:
        ans.append(i)
if len(ans) > 0:
    for i in range(len(ans)):
        print(ans[i])
else:
    print(-1)