## 이분 검색이란?

이분 검색이란 이진 탐색, 바이너리 서치라고도 불린다. <br>
BigO : `O(log N)` <br>
성능상으로 볼 떼, sort() 함수가 log N의 성능을 가진다. <br>

오름차순으로 정렬된 배열에서 원하는 숫자(target)을 찾는 알고리즘이다. <br>

1. 배열 전체의 중간값을 target과 비교
2. 중간값이 target 값보다 크면 왼쪽 부분만 비교
3. 왼쪽부터 중간값을 다시 target과 비교 <br>

<img width="1000" alt="download1" src="https://user-images.githubusercontent.com/96654391/212608916-36beded8-f5ba-4f8e-ba7f-b5bbc5c664ff.png"> <br>

이런 느낌? 무느알?

```python
n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
start = 0
end = n - 1

while start <= end:
    mid = (end + start) // 2
    if nums[mid] == m:
        print(mid + 1)
        break
    elif nums[mid] < m:
        start = mid + 1
    elif nums[mid] > m:
        end = mid - 1
```

## 백준 1654 랜선 자르기

📌 [백준 1654 문제 링크](https://www.acmicpc.net/problem/1654) <br>

k개의 랜선을 가지고 있는데, N개의 같은 길이의 랜선을 만들고 싶다.

### 풀이 코드

```python
# 1654 랜선 자르기

# k개의 랜선을 가지고 있는데, N개의 같은 길이의 랜선을 만들고 싶다.

import sys

input = sys.stdin.readline
k, n = map(int, input().split())
lines = []
for _ in range(k):
    lines.append(int(input()))

start = 1
end = max(lines)

while start <= end:
    mid = (start + end) // 2  # 최대 길이가 mid일 때
    line_cnt = 0
    # 개수가 count
    for i in lines:
        line_cnt += i // mid

    if line_cnt >= n:
        start = mid + 1
    else:
        end = mid - 1
print(end)

```

### 코드 설명

기존 이분 탐색의 코드에서 구하고자 하는데 필요한 랜선 개수를 구하기 위해 for 문을 사용 <br>

이 문제에서 mid 자체가 잘라야되는 랜선으로 활용이 되었다. 이분 탐색을 풀기 위해서는 mid 라는게 어떤거를 의미하고 어떻게 사용해야될지를 잘 생각해봐야될 것 같다.



## 백준 20444 색종이와 가위

📌 [백준 20444 문제 링크](https://www.acmicpc.net/problem/20444) <br>

n번의 가위질로 k개의 색종이 조각을 만들 수 있다면 YES, 아니라면 NO를 출력

### 실패 코드

```python
# 20444 색종이와 가위

# n번의 가위질로 k개의 색종이 조각을 만들 수 있다면 YES, 아니라면 NO를 출력

import sys

input = sys.stdin.readline
n, k = map(int, input().split())
# 1번 자름 -> 2개
# 2번 자름 -> 4개
# 3번 자름 -> 6개
# 4번 자름 -> 9개 / 8개
start = 1
end = k
count = 0
while start != end:
    mid = (start + end) // 2
    end = mid
    count += 1
    # print(start, end)
if count == n:
    print('YES')
else:
    print('NO')
```

mid 가 의미하고 있는게 무엇인지 중요한 것 같다... 뭐를 의미하고 있는거지,,,?

### 풀이 코드

```python
# 20444 색종이와 가위

# n번의 가위질로 k개의 색종이 조각을 만들 수 있다면 YES, 아니라면 NO를 출력

import sys

input = sys.stdin.readline
n, k = map(int, input().split())
# 1번 자름 -> 2개
# 2번 자름 -> 4개
# 3번 자름 -> 6개
# 4번 자름 -> 9개 / 8개
start = 0
end = n // 2
isPossible = False

# 가위질을 가로로 자른 횟수와 세로로 자른 횟수로 나뉨
# = 조각 개수는 (row_cut + 1) * (col_cut + 1)

# 거기에다가 row_cut과 col_cut은 대칭적이기 때문에 row_cut 기준으로 n // 2만큼 확인하면 됨
while start <= end:
    row_cut = (start + end) // 2 # mid라는게 가로로 자르는 횟수로 봄
    col_cut = n - row_cut

    pieces = (row_cut + 1) * (col_cut + 1)
    if k == pieces:
        print('YES')
        isPossible = True
        break
    if k > pieces:
        start = row_cut + 1
    else:
        end = row_cut - 1

if not isPossible:
    print('NO')

```
mid라는게 가로로 자르는 횟수로 봄. 

### 코드 설명


가위질을 가로로 자른 횟수와 세로로 자른 횟수로 나뉨 = 조각 개수는 (row_cut + 1) * (col_cut + 1) <br>

거기에다가 row_cut과 col_cut은 대칭적이기 때문에 row_cut 기준으로 n // 2만큼 확인하면 됨 <br>

잘려진 횟수가 k보다 적다는 것은 행으로 자른 횟수가 너무 적다는 것이므로 행 자르는 횟수를 늘린다. <br>
반대로 k보다 많다는 것은 행으로 자른 횟수는 줄이고 열로 자른 횟수를 늘려야된다는 것이다. <br>

이분 탐색이라는 주제 자체가 코드 상으로 이해는 쉬운데 그걸 이해하는 게 어렵다. 특히 mid를 어떻게 이해하고 어떤 식으로 활용해서 break 문을 만들 것인지가 중요한듯?