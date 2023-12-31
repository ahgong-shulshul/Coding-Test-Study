## 백준 11660 구간 합 구하기 5

📌 [백준 11660 문제 링크](https://www.acmicpc.net/problem/11660) <br>

(x1, y1)부터 (x2, y2)까지 합을 구하는 프로그램 작성하기

### 실패 코드

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

### 풀이 코드

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

### 코드 설명

📌 [참고 링크](https://sodehdt-ldkt.tistory.com/76) <br>

![Alt text](img1.daumcdn.png) <br>

뭐 이런 느낌으로 누적합을 사용한다고 한다. 아니 근데 코드가 짜기 어렵다기 보다는 에바야 ㅜㅜ 어케 생각하누

## 백준 2156 포도주 시식

📌 [백준 2156 문제 링크](https://www.acmicpc.net/problem/2156) <br>

연속으로 놓여져 있는 포도주 잔에서 최대의 양을 마실 수 있다. 최대의 양을 출력하는 프로그램

### 풀이 코드

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

### 코드 설명

규칙에 따라서 wine(입력값)과 dp(합)을 사용을 하는건데 동적 계획법은 이런식으로 진행을 하는 것 같다. <br>

+a. `dp = [0] * 10000` 이런 느낌으로 입력을 받는다면 인덱스 에러를 줄일 수 있다.

## 백준 2293 동전 1

📌 [백준 2293 문제 링크](https://www.acmicpc.net/problem/2293) <br>

n가지 종류의 동전 -> 가치의 합이 k원이 되도록하고 싶다. 그 경우의 수는?

### 풀이 코드

```python
# 2293 동전 1

# n가지 종류의 동전 -> 가치의 합이 k원이 되도록하고 싶다. 그 경우의 수는?

import sys

input = sys.stdin.readline
n, k = map(int, input().split())
value = [int(input()) for i in range(n)]

dp = [0] * (k+1)
dp[0] = 1
# dp[k] 가 답이 될 수 있도록
for i in value:
    for j in range(i, k+1):
        if j-i >= 0:
            dp[j] += dp[j-i]
        # print(dp)
print(dp[k])
```

### 코드 설명

```python
dp[k] 가 답이 될 수 있도록
10 -> 5, 5 -> 1/2/2 5 -> 1/1/1/2 5 -> 1/1/1/1/1 5 -> 1/2/2 1/2/2 -> 1/2/2 1/1/1/2 -> 1/2/2 1/1/1/1/1 -> 1/1/1/2 1/2/2
0 1 1 0 0 1 0 0 0 0 0 #한 개로 만들 수 있는 가치
0 1 2(1(기존방법)+1(추가된 방법)) 1(0(기존방법)+1+1-1) 1 1 1 1 0 0 1 #두 개로 만들 수 있는 가치
0 1 2 2 2 2 2 2 1 1 1 #세 개로 만들 수 있는 가치
```

나는 동전 1개로 해당 가치를 만들 수 있는 방법 -> 2개로 해당 가치를 만들 수 있는 방법,,, <br>

이렇게 하려고 했는데 아무리 해도 규칙을 못찾아서 찾아보니까 1원을 무조건 썼을 때 해당 가치를 만들 방법, 2원을 무조건 썼을 때 해당 가치를 만들 방법 ,, 이런식으로 했다,, <br>

아쉽다 거의 했는데,,,,😢

## 백준 2294 동전 2

📌 [백준 2294 문제 링크](https://www.acmicpc.net/problem/2294) <br>

가치 합이 k원이 되면서 동전의 개수가 최소가 되도록 하려면 동전은 몇 개가 되는지.

### 실패 코드

```python
# 2294 동전 2

# 가치 합이 k원이 되면서 동전의 개수가 최소가 되도록 하려면 동전은 몇 개가 되는지.

import sys

input = sys.stdin.readline
n, k = map(int, input().split())
value = [int(input()) for i in range(n)]
value.sort(reverse=True)
dp = [0] * (k+1)
dp[0] = 1
min_cnt = float('inf')
for i in range(n):
    # i원을 사용했을 때의 개수
    cnt = 0
    temp_val = k
    # print('value:', value[i], 'cnt:', cnt)
    while temp_val > 0:
        # print('temp_val:', temp_val)
        temp_val -= value[i]
        cnt += 1
        for j in range(i, n):
            # print('temp_val:', temp_val)
            if temp_val % value[j] == 0:
                cnt += (temp_val // value[j])
                temp_val -= value[j] * (temp_val // value[j])
                break
    if temp_val == 0 and (cnt < min_cnt):
        min_cnt = cnt
    # print(min_cnt)
    # print('----------')
if min_cnt == float('inf'):
    print(-1)
else:
    print(min_cnt)
```

`정답 3%`

### 실패 코드

```python
# 2294 동전 2

# 가치 합이 k원이 되면서 동전의 개수가 최소가 되도록 하려면 동전은 몇 개가 되는지.

import sys

input = sys.stdin.readline
n, k = map(int, input().split())
value = [int(input()) for i in range(n)]

dp = [100000] * (k+1)
for i in value:
    dp[i] = 1

for i in range(min(value)+1, k+1):
    temp = []
    temp.append(dp[i])
    for j in value:
        if (dp[i-j] < 100000) and i-j >= 0:
            temp.append(dp[i-j] + 1)
            # print(temp)
    dp[i] = min(temp)
    # print(dp)

print(dp[k] if dp[k] < 100000 else -1)
```

해당 가치를 만들기 위해서 필요한 동전 개수 = 만들어진 가치에서의 동전 개수 + 1(가치가 만들어질 수 있다면!) -> ex <br>

```txt
가치 (1~k)
0  1  2  3  4  5  6  7  8  9
   1  2  3  4  1  2  3  4  5
```

근데 `런타임 에러` ,,, 인덱스 에러 같은데,, 뭐가 문제지? <br>

반례 발견

```txt
1 2
3
```

이라면 -1이 나와야되는데 인덱스 에러 발생

### 실패 코드

```python
# 2294 동전 2

# 가치 합이 k원이 되면서 동전의 개수가 최소가 되도록 하려면 동전은 몇 개가 되는지.

import sys

input = sys.stdin.readline
n, k = map(int, input().split())
value = [int(input()) for i in range(n)]

dp = [100001] * (10000+1)
# print(dp)
for i in value:
    dp[i] = 1

for i in range(min(value)+1, k+1):
    temp = []
    temp.append(dp[i])
    for j in value:
        if (i-j >= 0) and (dp[i-j] <= 100001):
            temp.append(dp[i-j] + 1)
            # print(temp)
            print(dp[i-j])
    dp[i] = min(temp)
    print(dp)

print(dp[k] if dp[k] < 100001 else -1)
```

구해야되는 가치가 입력된 가치보다 작다면 원소 개수가 작기 때문에 인덱스 에러가 발생했었음.. 그런데도 `런타임 에러` 왜????

### 풀이 코드

```python
# 2294 동전 2

# 가치 합이 k원이 되면서 동전의 개수가 최소가 되도록 하려면 동전은 몇 개가 되는지.

import sys

input = sys.stdin.readline
n, k = map(int, input().split())
value = [int(input()) for i in range(n)]

dp = [100001] * (100000+1)
# print(dp)
for i in value:
    dp[i] = 1

for i in range(min(value)+1, k+1):
    temp = []
    temp.append(dp[i])
    for j in value:
        if (i-j >= 0) and (dp[i-j] <= 100001):
            temp.append(dp[i-j] + 1)
            # print(temp)
    dp[i] = min(temp)
    # print(dp)

print(dp[k] if dp[k] < 100001 else -1)
```

허,, ㅁㅊㅁㅊㅁ!!! 최대 가치값이 맞지 않아서 틀렸던 거였다...!

### 코드 설명

해당 인덱스(==가치)로 만들 수 있는 동전 개수를 dp에 저장한다. dp[k]가 정답이 되도록!
