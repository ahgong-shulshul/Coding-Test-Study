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



## 백준 2805 나무 자르기

📌 [백준 2805 문제 링크](https://www.acmicpc.net/problem/2805) <br>

높이 h 지정 -> 모두 잘라 -> 필요한 만큼만 집으로 가져가려고 하는데, 이때 적어도 M미터의 나무를 집에 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램

## 실패 코드

```python
# 2805 나무 자르기

# 높이 h 지정 -> 모두 잘라 -> 필요한 만큼만 집으로 가져가려고 하는데, 이때 적어도 M미터의 나무를 집에 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
height = [int(i) for i in input().split()]

start = 1
end = max(height)
isPossible = False
while start <= end:
    mid = (start + end) // 2
    get = 0
    # 얻은 나무의 길이 구하기
    for i in range(n):
        # 나무가 자를 길이보다 짧다면 얻을 수 있는 길이가 없음.
        if height[i] - mid >= 0:
            get += height[i] - mid
    if get == m:
        print(mid)
        break
    if get < m:
        end = mid - 1
    else:
        start = mid + 1
```

`정답(2%)` <br>

반례 <br>
```
3 4
3 3 5
``` 

필요한 길이랑 가장 비슷하게 잘라야되는 길이는 2이다.... 하지만 출력은 안되고 while 문 조건때문에 출력은 안되고 반복문이 끝남. <br>

## 실패 코드

```python
# 2805 나무 자르기

# 높이 h 지정 -> 모두 잘라 -> 필요한 만큼만 집으로 가져가려고 하는데, 이때 적어도 M미터의 나무를 집에 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
height = [int(i) for i in input().split()]

start = 1
end = max(height)
mid = 0
while start <= end:
    mid = (start + end) // 2
    get = 0
    # 얻은 나무의 길이 구하기
    for i in range(n):
        # 나무가 자를 길이보다 짧다면 얻을 수 있는 길이가 없음.
        if height[i] - mid >= 0:
            get += height[i] - mid
    # print(get, m)
    if get == m:
        
        break
    if get < m:
        end = mid - 1
    else:
        start = mid + 1

print(mid)
``` 

무조건 나무를 가져가야되므로 반드시 잘린 나무가 M일 필요는 없음. <br>

```
10 1
600000000 600000000 600000000 600000000 600000000 600000000 600000000 600000000 600000000 600000000
```

반례 발견 <br>

만약 저렇게 입력이 된다면 `59999999` 이 나와야 되는데, 나는 `600000000` 이 나온다. 
  
## 실패 코드

```python
# 2805 나무 자르기

# 높이 h 지정 - > 모두 잘라 - > 필요한 만큼만 집으로 가져가려고 하는데, 이때 적어도 M미터의 나무를 집에 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
height = [int(i) for i in input().split()]

# 4 8
# 20 15 10 17

start = 1
end = max(height)
mid = 0
get = 0
while start < end:
    mid = (start + end) // 2
    # 얻은 나무의 길이 구하기# 나무가 자를 길이보다 짧다면 얻을 수 있는 길이가 없음.
    get = sum([(t - mid) if t - mid > 0 else 0 for t in height])

    # print(get, m, '자른 길이:', mid)
    if get == m:
        break
    if get < m:
        end = mid - 1
    else :
        start = mid + 1

print(mid)
```

여튼 자른게 나와야되긴 하니까 while 문 조건에 =을 붙히지는 않음. 근데 `정답입니다(6%)` 아니 뭐가 문제세여?????

## 정답 코드

아씨,, 댕 어이없네,,,,,, 마지막에 mid를 출력하는게 아닌 end를 출력,,,,,,,,,,,,,ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ <br>

추가적으로 나무는 무조건 잘라야되므로 `get` 이 구해야되는 나무길이보다 길더라도 m과 가장 비슷한 길이를 구해야되므로 중간에 break 문 없이 계속 이분탐색을 돌리면 됨...

```python
# 2805 나무 자르기

# 높이 h 지정 - > 모두 잘라 - > 필요한 만큼만 집으로 가져가려고 하는데, 이때 적어도 M미터의 나무를 집에 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
height = [int(i) for i in input().split()]

# 4 8
# 20 15 10 17

start = 1
end = max(height)

while start <= end:
    mid = (start + end) // 2
    # 얻은 나무의 길이 구하기
    # 나무가 자를 길이보다 짧다면 얻을 수 있는 길이가 없음.
    get = sum([(t - mid) if t - mid > 0 else 0 for t in height])

    # print(get, m, '자른 길이:', mid)
    if get >= m:
        start = mid + 1
        
    elif get < m:
        end = mid - 1

print(end)
```

## 코드 설명

일반적인 이분 탐색 문제이다. 당연히 자르려고 하는 나무의 길이를 mid로 두고 자를 길이에 대한 반복문을 통해서 얻은 나무의 길이와 필요한 나무의 길이를 비교해서 다시 이분 탐색을 진행한다.