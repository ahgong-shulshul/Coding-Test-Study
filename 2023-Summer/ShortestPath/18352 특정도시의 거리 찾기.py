"""
첫째 줄에 도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시의 번호 X가 주어진다. 
(2 ≤ N ≤ 300,000, 1 ≤ M ≤ 1,000,000, 1 ≤ K ≤ 300,000, 1 ≤ X ≤ N) 
둘째 줄부터 M개의 줄에 걸쳐서 두 개의 자연수 A, B가 공백을 기준으로 구분되어 주어진다. 
이는 A번 도시에서 B번 도시로 이동하는 단방향 도로가 존재한다는 의미다. (1 ≤ A, B ≤ N) 단, A와 B는 서로 다른 자연수이다.
"""

import sys
from collections import deque

input = sys.stdin.readline      #아직도 sys로 입력 받는거 너무 어색하다..

# N 도시 수, M 도로 수, K 거리 정보 X 출발 도시
N, M, K, X = map(int, input().split(' '))
graph = [[] for _ in range(N+1)]

# 도시 거리 정보 입력받기
for _ in range(M):
  a, b =  map(int, input().split(' '))  
  graph[a].append(b)

#모든 도시에 대한 거리 정보 초기화
distance = [-1] *(N+1)
distance[X] = 0 # 출발 도시까지의 거리는 0으로 설정

#너비 우선 탐색 수행
q = deque([X])
while q:
  now = q.popleft()
  #현재 도시에서 이동할 수 있는 모든 도시 확인
  for next_node in graph[now]:
        #아직 방문하지 않은 도시
        if distance[next_node] == -1:
           #최단거리 갱신
           distance[next_node] = distance[now] + 1
           q.append(next_node)

#최단 거리가 k인 모든 도시의 번호를 오름차순으로 출력
check = False
for i in range(1,N+1):
   if distance[i] == K:
        print(i)
        check = True
#최단 거리가 k인 도시가 없다면 -1 출력
if check == False:
    print(-1)