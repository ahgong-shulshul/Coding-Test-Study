## 백준 11660 구간 합 구하기 5

📌 [백준 11660 문제 링크](https://www.acmicpc.net/problem/11660) <br>

(x1, y1)부터 (x2, y2)까지 합을 구하는 프로그램 작성하기

## 실패 코드

```python
# 11660 구간 합 구하기 5

# (x1, y1)부터 (x2, y2)까지 합을 구하는 프로그램 작성하기

import sys

input = sys.stdin.readline
n, m = map(int, input().split())
# m은 합을 구해야되는 횟수
grid = [[int(i) for i in input().split()] for _ in range(n)]
pos = []
for i in range(m):
    temp = [int(i) for i in input().split()]
    temp2 = []
    # 인덱스 0 ~ n - 1까지
    temp2.append((temp[0] - 1, temp[1] - 1))
    temp2.append((temp[2] - 1, temp[3] - 1))
    pos.append(temp2)

for i in range(m):
    row1, col1 = pos[i][0]
    row2, col2 = pos[i][1]
    sum = 0
    for j in range(row1, row2 + 1):
        for k in range(col1, col2 + 1):
            sum += grid[j][k]
    print(sum)
```

역시 `시간 초과` <br>

## 풀이 코드

```python
# 11660 구간 합 구하기 5

# (x1, y1)부터 (x2, y2)까지 합을 구하는 프로그램 작성하기

import sys

input = sys.stdin.readline
n, m = map(int, input().split())
# m은 합을 구해야되는 횟수
grid = [[int(i) for i in input().split()] for _ in range(n)]

accum_grid = [[0] * (n+1) for i in range(n+1)]
# 누적합 구하기
for i in range(1, n+1):
    for j in range(1, n+1):
        accum_grid[i][j] = accum_grid[i][j-1] + \
            accum_grid[i-1][j] - accum_grid[i-1][j-1] + grid[i-1][j-1]
        # print(accum_grid)

for k in range(m):
    row1, col1, row2, col2 = map(int, input().split())
    result = accum_grid[row2][col2] - accum_grid[row2][col1-1] - \
        accum_grid[row1-1][col2] + accum_grid[row1-1][col1-1]
    print(result)

```

## 코드 설명

📌 [참고 링크](https://sodehdt-ldkt.tistory.com/76) <br>

![Alt text](img1.daumcdn.png) <br>

뭐 이런 느낌으로 누적합을 사용한다고 한다. 아니 근데 코드가 짜기 어렵다기 보다는 에바야 ㅜㅜ 어케 생각하누




## 백준 2156 포도주 시식

📌 [백준 2156 문제 링크](https://www.acmicpc.net/problem/2156) <br>

연속으로 놓여져 있는 포도주 잔에서 최대의 양을 마실 수 있다. 최대의 양을 출력하는 프로그램

## 풀이 코드

```python
# 2156 포도주 시식

# 연속으로 놓여져 있는 포도주 잔에서 최대의 양을 마실 수 있다. 최대의 양을 출력하는 프로그램

import sys

input = sys.stdin.readline
n = int(input())
wine = [0] * 10000
for i in range(n):
    wine[i] = int(input())
# 이것도 부분합처럼 규칙이 있지 않을까?
# 6 10 13 9 8 1
dp = [0] * 10000
dp[0] = wine[0]
dp[1] = wine[0] + wine[1]
# 6 16 23 9
dp[2] = max(wine[2]+wine[0], wine[2]+wine[1], dp[1])
for i in range(3, n):
    dp[i] = max(wine[i]+dp[i-2], wine[i]+wine[i-1]+dp[i-3], dp[i-1])

print(max(dp))
```

## 코드 설명

규칙에 따라서 wine(입력값)과 dp(합)을 사용을 하는건데 동적 계획법은 이런식으로 진행을 하는 것 같다. <br>

+a. `dp = [0] * 10000` 이런 느낌으로 입력을 받는다면 인덱스 에러를 줄일 수 있다.