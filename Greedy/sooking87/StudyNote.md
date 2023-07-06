## 그리디 알고리즘

- 그리디 알고리즘은 탐욕법이라고도 하며, 현재 상황에서 지금 당장 좋은 것만 고르는 방법
- 일반적인 그리디 알고리즘은 문제를 풀기 위한 최소한의 아이디어를 떠올릴 수 있는 능력을 요구

## 백준 11047 동전 0

📌 [백준 11047 문제 링크](https://www.acmicpc.net/problem/11047) <br>

N개의 동전의 가치를 입력받고, K의 가치를 만들기

### 풀이 코드

```python
# 11047 동전 0

# N개의 동전의 가치를 입력받고, K의 가치를 만들기

n, k = map(int, input().split(' '))
values = []
for _ in range(n):
    values.append(int(input()))

# 가치가 큰 동전부터 K의 가치를 채울 수 있는지 확인
i = n - 1
cnt = 0
while True:
    # k보다 큰 가치라면 -> 그보다 작은 가치랑 비교 필요(--)
    if values[i] > k:
        i -= 1
    # k보다 작은 가치라면 -> values[i]로 나눈 나머지부터 다시 개수 세야됨
    else:
        cnt += k // values[i]
        k = k % values[i]
    if k == 0:
        break
print(cnt)
```

### 코드 설명

k보다 values[i]가 작다면 일단은 나누어지므로 그것만큼 개수를 count하고, 그 다음 나머지를 다시 values[i]랑 비교하면서 개수를 세어나아간다.

## 백준 14916 거스름돈

📌 [백준 14916 문제 링크](https://www.acmicpc.net/problem/14916) <br>

거스름돈 동전의 개수가 최소가 되도록 거슬러주기

### 풀이 코드

```python
# 14916 거스름돈

# 거스름돈 동전의 개수가 최소가 되도록 거슬러주기

coins = [5, 2]
money = int(input())
count = 0

while True:
    # 5원부터 거스름돈 구하기 -> 최소가 되기 위함
    if money % 5 == 0:
        count += money // 5
        money = 0
    # 거스를 수 없으면(음수) -> -1 출력
    # 거스를 수 있으면(0) -> count 출력
    if money < 0:
        print(-1)
        break
    elif money == 0:
        print(count)
        break
    # 5원을 못거스르면 2원씩 빼기
    money -= 2
    count += 1
```

### 코드 설명

5원으로 나뉘어진다면 `money // 5` 만큼 나누어 주는게 BEST <br>
그게 아니라면 2월을 빼보고 다시 5원으로 나누어지는지 확인(5로 나누어지는게 BEST기 때문)

## 백준 11000 강의실 배정

📌 [백준 11000 문제 링크](https://www.acmicpc.net/problem/11000) <br>

강의실을 최소로 개설

### 풀이 코드

```python
# 11000 강의실 배정

# 강의실을 최소로 개설

import heapq
import sys

# 입력받기
input = sys.stdin.readline  # 얘의 용도?
n = int(input())
classes = []
for _ in range(n):
    temp = list(map(int, input().split()))
    classes.append(temp)

# 정렬순: S -> T 즉, S순으로 정렬 후 수업 진행 시간이 작은 순대로 정렬됨
classes.sort()
heap = []
heapq.heappush(heap, classes[0][1])  # 첫 번째 강의가 끝나는 시간을 넣음

for i in range(1, n):
    if heap[0] > classes[i][0]:
        heapq.heappush(heap, classes[i][1])
    if heap[0] <= classes[i][0]:
        heapq.heappop(heap)
        heapq.heappush(heap, classes[i][1])
print(len(heap))
```
#### ❓sys.stdin.readline의 용도

input()은 문자열 변환, 줄 바꿈 제거 등 추가적인 과정이 있고, 데이터가 하나씩 버퍼에 들어가는 반면, sys.stdin.readline()은 문자열로 변환, 줄 바꿈 과정이 없으며 데이터가 한 번에 버퍼에 들어가므로

sys.stdin.readline()이 input()보다 빠르다.

#### ❓정렬을 해야되는데 왜 heap을 사용하였나

heapq 모듈은 왜 빠를까?
PriorityQueue & heapq / 우선순위큐와 힙큐 <br>

heap 모듈의 경우는 속도도 빨라서 직접 구현한 힙 클래스로는 시간초과 문제를 해결할 수 있다. 우선순위 큐는 heapq를 활용한 모듈이다. 근데 queue 속 PriorityQueue는 Tread-Safe하고, heapq는 Non-safe하다. 즉, safe한지 아닌지 확인 절차가 필요하므로 속도가 더 느리다. <br>

또한 heapq는 리스트를 힙처럼 사용할 수 있다.

### 코드 설명

와 미친,,, 실패코드 위쪽 주석을 확인해보면 문제 해석하기 전까지도 문제 이해 잘못함,,,, -> ㅄ,,,,? <br>

수강 신청 할 수 있는 최대의 강의수를 찾는게 아니라 강의실을 최소로 개설하는 것이 문제였다,,,
결국, 끝나는 시간과 시작하는 시간을 비교하는 것은 맞았지만, 경우의 수가 조금 달랐다. <br>

시작하는 순으로 정렬을 했을 때 <br>

끝나는 시간(heap[0]) <= 시작 시간(classes[i][0]): 기존 강의실에 개설 가능 <br>
끝나는 시간(heap[0]) > 시작 시간(classes[i][0]): 새로운 강의실 개설 필요 <br> 
결국 heap[0]은 가장 빨리 끝나는 강의 시간, heap[1], heap[2],,,는 가장 빨리 시작하는 강의 시간의 끝나는 시간이 min-heap 구조로 정렬이 된다.



## 백준 19598 최소 회의실 개수

📌 [백준 19598 문제 링크](https://www.acmicpc.net/problem/19598) <br>

N개의 회의를 모두 진행할 수 있는 최소 회의실 개수 구하기

### 실패 코드

```python
# 19598 최소 회의실 개수

# N개의 회의를 모두 진행할 수 있는 최소 회의실 개수

import sys
import heapq

input = sys.stdin.readline
n = int(input())
meetings = []
for _ in range(n):
    temp = [int(i) for i in input().split()]
    meetings.append(temp)

meetings.sort()
heap = []
heapq.heappush(heap, meetings[0][1])

for i in range(1, n):
    if meetings[i][0] > heap[0]:
        heapq.heappush(heap, meetings[i][1])
    if meetings[i][0] <= heap[0]:
        heapq.heappop(heap)
        heapq.heappush(heap, meetings[i][1])
print(len(heap))

```

저번 강의실 배정 문제랑 똑같아서 똑같이 풀었는데 틀림,,, 왜지?

### 풀이 코드

```python
# 19598 최소 회의실 개수

# N개의 회의를 모두 진행할 수 있는 최소 회의실 개수

import sys
import heapq

input = sys.stdin.readline
n = int(input())
meetings = []
for _ in range(n):
    temp = [int(i) for i in input().split()]
    meetings.append(temp)

meetings.sort()
heap = []
heapq.heappush(heap, meetings[0][1])

for i in range(1, n):
    if meetings[i][0] < heap[0]:
        heapq.heappush(heap, meetings[i][1])
    if meetings[i][0] >= heap[0]:
        heapq.heappop(heap)
        heapq.heappush(heap, meetings[i][1])

print(len(heap))

```

아래 조건문 부등호를 잘못한 것이었다. 그리고 저 조건문 두 개의 순서가 바뀌면 안됨 <br>

왜냐면 heappop을 한 다음 다시 `meetings[i][0] < heap[0]` 을 판별을 하기 때문에,, 아니면 elif로 해도 괜찮다!

### 코드 설명

강의실 배정 문제랑 알고리즘은 동일하다.
