# 동적 계획법

📌 [참고 링크](https://velog.io/@bonjaski0989/%EB%8F%99%EC%A0%81%EA%B3%84%ED%9A%8D%EB%B2%95Dynamic-Programming-%EC%A0%95%EB%A6%AC%EA%B8%80Python) <br>

이미 진행이 되었던 연산이 반복되는 결점을 보안하기 위해 동적 계획법이 고안되었다. <br>

- 메모이제이션(Top-Down, 하향식)
- 테이블화(Bottom-Up, 상향식)

## 보통 어떤 문제에 적용?

소문제의 결과를 다른 소문제를 푸는데 사용되는 풀이법 <br>

- 동적 계획법: 소문제 종속적(소문제가 상위 문제에 영향을 끼치며 원소들이 종속적) / Always 최적의 결과 도출
- 분할 정복: 소문제 독립적(퀵정렬, 병합 정렬)
- 그리디: '현 상태'에 대해서 최적의 경우를 판단하므로 최적해가 구해지지 않을 수 있음

---

title: "[백준 1463][DynamicProgramming1] 1로 만들기"
excerpt: "[백준 1463][DynamicProgramming1] 1로 만들기"
categories: [Algorithm Python]
tags: [Algorithm Study, Python, Algorithm, Backjoon]
toc: true
toc_sticky: true

---

## 백준 1463 거스름돈

📌 [백준 1463 문제 링크](https://www.acmicpc.net/problem/1463) <br>

X가 3으로 나누어 떨어지면 3으로 나눈다. X가 2로 나누어 떨어지면 2로 나눈다. 1을 뺀다.

### 풀이 코드

```python
# 1463 1로 만들기

# X가 3으로 나누어 떨어지면 3으로 나눈다. X가 2로 나누어 떨어지면 2로 나눈다. 1을 뺀다.

import sys

input = sys.stdin.readline
n = int(input())
cnt = [0] * (n + 1)

# 그리디의 경우는 처음에 생각한 최적의 방법이 끝까지 반례없이 적용이 되는 경우다. 이런 경우는 무조건 n != 1일 떄까지 3으로 나누거나 2로 나누거나 1을 빼가면서 구해가면 된다.
# 하지만 이 문제의 경우 10 -> 5 -> 4 -> 2 -> 1 보다는 10 -> 9 -> 3 -> 1이 최솟값을 가진다.
# 메모이제이션 방법은 중복해 계산되는 값을 저장해 효율을 높여준다.
for i in range(2, n + 1):
    cnt[i] = cnt[i - 1] + 1 # i - 1에서 1을 더하는 연산 횟수
    # cnt[1]은 1이 1이 되는데 필요한 연산 횟수
    # cnt[2]는 2가 1이 되는데 필요한 연산 횟수
    # cnt[i]는 i가 1이 되는데 필요한 연산 횟수
    if i % 3 == 0:
        cnt[i] = min(cnt[i], cnt[i // 3] + 1) # i // 3까지의 연산 횟수 + i를 3으로 나누는 연산 횟수(1회)
    if i % 2 == 0:
        cnt[i] = min(cnt[i], cnt[i // 2] + 1) # i // 2까지의 연산 횟수 + i를 2으로 나누는 연산 횟수(1회)
    # print(cnt)
print(cnt[n])
```

### 코드 설명

위 코드 내 주석 처리 참고,,, <br>

<small>뒈지게 어렵네 ㅡㅡ</small>

## 백준 1890 점프

📌 [백준 1890 문제 링크](https://www.acmicpc.net/problem/1890) <br>
N×N 게임판: 0은 종착점, 항상 현재 칸에 적혀있는 수만큼 오른쪽이나 아래로 가야된다. -> (0, 0) 위치에서 규칙에 맞게 이동할 수 있는 경로의 개수

### 대충 코드

```python
# 1890 점프

# N×N 게임판: 0은 종착점, 항상 현재 칸에 적혀있는 수만큼 오른쪽이나 아래로 가야된다. -> (0, 0) 위치에서 규칙에 맞게 이동할 수 있는 경로의 개수

import sys


def row_first(cnt, col, row):
    # print(cnt, col, row)
    if col == n - 1 and row == n - 1:
        print("끝", cnt)
        cnt[col][row] += 1

        print(cnt, col, row)
        ans = cnt[col][row]
        return ans
    temp_row = row + board[col][row]
    temp_col = col + board[col][row]
    if temp_row >= 0 and temp_row < n:  # 오른쪽으로 이동 = 열 이동
        cnt[col][board[col][row]] += 1
        row += board[col][row]
        print('오른쪽으로 이동', cnt, col, row)
        return row_first(cnt, col, row)
    if temp_col >= 0 and temp_col < n:  # 아래로 이동 = 행 이동
        cnt[board[col][row]][row] += 1
        col += board[col][row]
        print('아래쪽으로 이동', cnt, col, row)
        return row_first(cnt, col, row)


def col_first(cnt, col, row):
    # print(cnt, col, row)
    if col == n - 1 and row == n - 1:
        print("끝", cnt)
        cnt[col][row] += 1

        print(cnt, col, row)
        ans = cnt[col][row]
        return ans
    temp_row = row + board[col][row]
    temp_col = col + board[col][row]

    if temp_col >= 0 and temp_col < n:  # 아래로 이동 = 행 이동
        cnt[board[col][row]][row] += 1
        col += board[col][row]
        print('아래쪽으로 이동', cnt, col, row)
        return col_first(cnt, col, row)
    if temp_row >= 0 and temp_row < n:  # 오른쪽으로 이동 = 열 이동
        cnt[col][board[col][row]] += 1
        row += board[col][row]
        print('오른쪽으로 이동', cnt, col, row)
        return col_first(cnt, col, row)


input = sys.stdin.readline
n = int(input())
board = [[int(i) for i in input().split()] for _ in range(n)]
cnt = [[0 for i in range(n)] for _ in range(n)]
col = 0
row = 0
result = 0
result += row_first(cnt, col, row)
result += col_first(cnt, col, row)
print("결과 도출:", result)
```

뭐 나름.. 메모이제이션을 공부를 해보고 cnt에서 간 데를 1씩 늘리면서 최종 (n, n)위치의 값을 출력하고자 함. <br>

근데 오른쪽으로 가는 방법과 아래쪽으로 가는 방법 두 가지가 있는데, 그걸 어케 해야될지 모르겠음. -> 제일 깊이 까지 내려갔다가 올라오는 식.. 이런거 했는데 무슨 문제였더라.

### 풀이 코드

```python
# 1890 점프

# N×N 게임판: 0은 종착점, 항상 현재 칸에 적혀있는 수만큼 오른쪽이나 아래로 가야된다. -> (0, 0) 위치에서 규칙에 맞게 이동할 수 있는 경로의 개수

import sys

input = sys.stdin.readline
n = int(input())
board = [[int(i) for i in input().split()] for _ in range(n)]
cnt = [[0 for i in range(n)] for _ in range(n)]
cnt[0][0] = 1  # 초기 값

for col in range(n):
    for row in range(n):
        if col == n - 1 and row == n - 1:
            print(cnt[col][row])
            break
        # 오른쪽으로 이동
        if row + board[col][row] < n:
            cnt[col][row + board[col][row]] += cnt[col][row]

        # 아래쪽으로 이동
        if col + board[col][row] < n:
            cnt[col + board[col][row]][row] += cnt[col][row]
        # print(cnt, cnt[col][row], col, row)
```

아 생각했던거랑 비슷한데! 이중포문은 몰랐네,, 직접 하나하나 보면서 얘가 board 내에서 이동이 가능한지 아닌지만 보면 됐다. <br>

하지만 궁금한거는 왜 `cnt[col][row]` 만큼을 왜 더하는지 모르겠다. 1을 더하는 게 아니라,,, -> 현재까지 간 횟수만큼 다음 이동 칸으로 갈 수 있다.

### 코드 설명

규칙이 있었고, 2중 포문을 돌리면서 가능한 모든 경우의 수를 cnt에 하나씩 추가해나아갔다. <br>

여기서 이중 반복문의 DP를 알 수 있다.



## 백준 10844 쉬운 계단 수
📌 [백준 10844 문제 링크](https://www.acmicpc.net/problem/10844) <br>

옆 계단이 1차이가 나는 계단이 쉬운 계단이다. 길이가 n인 계단 수가 총 몇개 있는지, 1로 시작하는 계단수

## 실패 코드

```python
# 10844 쉬운 계단 수

# 옆 계단이 1차이가 나는 계단이 쉬운 계단이다. 길이가 n인 계단 수가 총 몇개 있는지, 1로 시작하는 계단수

import sys

input = sys.stdin.readline
n = int(input())  # n 자리수
# 10, 12, 21, 23, 32, 34, 43, 45, 54, 56, 65, 67, 76, 78, 87, 89, 98
cnt = 0
num = [0 for i in range(10**n + 1)]  # 계단은 1부터 시작
# n == 1: 10**1 전까지
# n == 2: 10**2 전까지
# print(num)
is_possible = True
for i in range(10**(n - 1), 10**n):  # 딱 n자리 수까지만
    str_num = str(i)
    for j in range(1, n):
        if abs(int(str_num[j - 1]) - int(str_num[j])) != 1:
            is_possible = False
            break
        is_possible = True
    if is_possible:
        cnt += 1

print(cnt)
```

`메모리 초과`

## 실패 코드

```python
# 10844 쉬운 계단 수

# 옆 계단이 1차이가 나는 계단이 쉬운 계단이다. 길이가 n인 계단 수가 총 몇개 있는지, 1로 시작하는 계단수

import sys

input = sys.stdin.readline
n = int(input())  # n 자리수
# 10, 12, 21, 23, 32, 34, 43, 45, 54, 56, 65, 67, 76, 78, 87, 89, 98

num = [0 for i in range(10**n + 1)]  # 계단은 1부터 시작
# n == 1: 10**1 전까지
# n == 2: 10**2 전까지
for i in range(1, 10):
    num[i] = 1
# 1차이가 나는 숫자들을 봤더니 2자리 수라면 쉬운 계단인 애들에서 3자리 수인 쉬운 계단이 되려면 10 자리수에서 차이가 1만 나는 애를 보면 된다.
is_possible = True
if n != 1:
    for i in range(10, 10**n):  # 딱 n자리 수까지만
        str_num = str(i)
        # print('str_num', str_num)
        start = len(str_num) - 2 # 2자리수면 1 3자리수면 2
        end = len(str_num) - 1 # 2자리수면 2 3자리수면 3

        if abs(int(str_num[start]) - int(str_num[end])) == 1:
            end_idx = len(str(i)) - 1 # n자리부터 n - 1자리까지
            if num[int(str(i)[0:end_idx])] == 1:
                num[i] = 1
                # print(i)
        
        # print('------------')
        # print(num)
cnt = len([i for i in num[10**(n - 1):10**n] if i == 1])
print(cnt % 1000000000)
```

2자리 부터 쉬운 계단인 경우를 체크한다. 왜냐하면 12는 쉬운 계단인데, 3자리인 경우의 쉬운 계단은 121, 123 이 쉬운 계단이므로 앞에 2자리수는 n == 2일때의 쉬운 계단과 동일, 맨 마지막 자리와 맨 마지막에서 두 번째 자리에 있는 숫자만 1차이가 나는지 확인하면 됨. 그래서 모든 쉬운 계단을 체크하고 해당 자리수에 해당하는 1을 카운트한다. <br>

근데 `메모리초과`  <br>

무조건 `num` 때문에 발생하는 건데 쟤를 어케 더이상 줄여?

## 풀이 코드


```python
# 10844 쉬운 계단 수

# 옆 계단이 1차이가 나는 계단이 쉬운 계단이다. 길이가 n인 계단 수가 총 몇개 있는지, 1로 시작하는 계단수

import sys

input = sys.stdin.readline
n = int(input())  # n 자리수

# dp 테이블 초기화,,
dp = [[0] * 10 for _ in range(n + 1)]

# 1의 자릿수의 경우의 수 초기화
for i in range(1, 10):
    dp[1][i] = 1

# 나머지 자릿수의 경우의 수 탐색
for i in range(2, n + 1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][1]
        elif 1 <= j <= 8:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
        else:
            dp[i][j] = dp[i-1][8]
print(sum(dp[n]) % 1000000000)
```

## 코드 설명


📌 [참고 링크](https://wooono.tistory.com/642) <br>

최소한의 규칙(점화식)을 발견하자,,,,,,,,,,,,,,,,,,, 규칙을 보게 되면 뒷 자리가 0인 경우는 앞에 1만 올 수 있음. <br>
뒤에 1~8이 오면 두 개가 올 수 있음. <br>
뒤에 9가 오면 앞에 8만 올 수 있음. <br>

```txt
각 자릿수에서 가장 뒤에 오는 숫자(0~9)
           0  1  2  3  4  5  6  7  8  9
자릿수(0)   0  0  0  0  0  0  0  0  0  0
자릿수(1)   0  1  1  1  1  1  1  1  1  1
자릿수(2)   1  1  2  2  2  2  2  2  2  1
자릿수(3)   1  3  3  4  4  4  4  4  3  2
``` 
가능한 횟수에 뒷자리만 비교를 하면 되는데(여기까지 비슷했는데) 0 / 1~8 / 9 의 규칙은 발견하지 못했다....고 한다.. 뭬친!

### 배운 점

DP는 최소한의 규칙/점화식을 발견하자! 심플하게 하면 할수록 정답에 가까워짐!