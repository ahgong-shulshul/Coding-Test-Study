## Shortest Path 알고리즘

### 다익스트라 알고리즘
* 여러 개의 노드가 존재할 때 특정 노드에서의 최단 경로를 찾아주는 알고리즘
* 그리디 알고리즘과 다이나믹 프로그래밍 알고리즘이 포함되어 있음

~~~python
# 방문하지 않은 노드 중 가장 최단거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    # 최단거리 테이블 갱신
    for j in graph[start]:
        distance[j[0]] = j[1]

    # 모든 노드에 대해 반복
    for i in range(n - 1):
        now = get_smallest_node()   # 현재 최단거리가 가장 짧은 노드를 꺼냄
        visited[now] = True         # 방문 처리
        
        for j in graph[now]:        # 선택된 노드와 연결된 다른 노드를 확인
            # 선택된 노드를 통해 가는 비용을 다시 계산
            # 선택된 노드의 비용 + 연결된 노드로 가는 비용
            cost = distance[now] + j[1]
            
            if cost < distance[j[0]]:   # 선택된 노드를 거쳐서 가는 비용이 더 짧은 경우
                distance[j[0]] = cost   # 최단거리 테이블 갱신
~~~


### 문제에 대한 풀이방법 정리
https://min02choi.github.io/categories/coding-test/baekjoon