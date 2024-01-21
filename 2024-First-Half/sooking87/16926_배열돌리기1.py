# 16926 배열 돌리기 1

# 첫 째줄 배욜의 크기 N, M, 회전의 수 R
# 둘 째줄 N개의 줄에 원소가 주어짐

# 2차원 -> 1차원으로 바꿔서 R 만큼 인덱스 수정

import sys
from collections import deque

input = sys.stdin.readline
n, m, r = map(int, input().split())
arr = []
deq = deque() # popleft를 통해서 O(1)을 사용하기 위해서
answer = [[0]*m for _ in range(n)]
loops = min(n, m) // 2

for i in range(n):
    temp = list(map(int, input().split()))
    arr.append(temp)

for i in range(loops):
    # 1차원 배열로 변환
    deq.clear()
    deq.extend(arr[i][i:m-i]) # 위쪽
    deq.extend([row[m-i-1] for row in arr[i+1:n-i-1]]) # 오른쪽
    deq.extend(arr[n-i-1][i:m-i][::-1]) # 아래쪽
    deq.extend([row[i] for row in arr[i+1:n-i-1]][::-1]) # 왼쪽

    deq.rotate(-r) # -r만큼 오른쪽으로(-이므로 왼쪽으로) 회전한다.
    for j in range(i, m-i):
        answer[i][j] = deq.popleft()
    for j in range(i+1, n-i-1):
        answer[j][m-i-1] = deq.popleft()
    for j in range(m-i-1, i-1, -1):
        answer[n-i-1][j] = deq.popleft()
    for j in range(n-i-2, i, -1):
        answer[j][i] = deq.popleft()

for row in answer:
    for col in row:
        print(col, end=' ')
    print()
    



