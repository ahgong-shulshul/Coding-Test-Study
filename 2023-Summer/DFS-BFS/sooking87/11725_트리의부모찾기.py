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
