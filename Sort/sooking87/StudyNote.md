## 백준 10814 나이순 정렬

📌 [백준 10814 문제 링크](https://www.acmicpc.net/problem/10814) <br>

나이순 오름차순 정렬 -> 나이가 같다면 가입한 순으로 한 줄에 한 명씩 출력

### 풀이 코드

```python
# 10814 나이순 정렬

# 나이순 오름차순 정렬 -> 나이가 같다면 가입한 순으로 한 줄에 한 명씩 출력

import sys

input = sys.stdin.readline
n = int(input())
people = []
for _ in range(n):
    age, name = input().split()
    temp = []
    temp.append(int(age))
    temp.append(name)
    people.append(temp)

people.sort(key=lambda x: x[0])  # 나이로만 정렬

for i in range(n):
    age, name = people[i]
    print(age, name)
```

### 코드 설명

`people.sort(key=lambda x: x[0])` lambda를 통해서 나이로만 정렬이 되고, 나이가 같은 경우는 입력받은 대로 정렬이 될 수 있도록 코딩함.

## 백준 2470 두 용액

📌 [백준 2470 문제 링크](https://www.acmicpc.net/problem/2470) <br>

### 실패 코드

```python
# 2470 두 용액

# 합쳐서 0에 가까운 두 용액을 출력

import sys
import math

input = sys.stdin.readline
n = int(input())
solution = [int(i) for i in input().split()]

solution.sort()
minus = 0
plus = len(solution) - 1
close_zero = math.inf
ans_minus = 0
ans_plus = 0
while True:
    while solution[plus] >= 0:
        temp = solution[minus] + solution[plus]
        if abs(close_zero) > abs(temp):
            close_zero = temp
            ans_minus = minus
            ans_plus = plus
        # print(solution[minus], solution[plus], temp)
        plus -= 1
    if minus >= plus:
        break
    minus += 1
    plus = len(solution) - 1
print(solution[ans_minus], solution[ans_plus])
```

`시간 초과` 에러 -> Greedy 방식. <br>

어떻게 하면 시간 초과를 해결할 수 있을까? heapq 사용??

### 실패 코드

```python
# 2470 두 용액

# 합쳐서 0에 가까운 두 용액을 출력

import sys
import math

input = sys.stdin.readline
n = int(input())
solution = [int(i) for i in input().split()]

solution.sort()
minus = 0
plus = len(solution) - 1
close_zero = math.inf
ans_minus = 0
ans_plus = 0
while True:
    while solution[plus] >= 0:
        temp = solution[minus] + solution[plus]
        if abs(close_zero) > abs(temp):
            close_zero = temp
            ans_minus = minus
            ans_plus = plus
        # 추가
        else:
            break
        # print(solution[minus], solution[plus], temp)
        plus -= 1
    if minus >= plus:
        break
    minus += 1
    plus = len(solution) - 1
print(solution[ans_minus], solution[ans_plus])

```

`틀렸습니다.....` <br>
여튼 위의 코드에서 heapq나 뭐 이런거를 써서 현재 O(n^2)인 복잡도를 O(nlogn)으로 줄일 수 있으면 좋을 것 같다. <br>

근데 sort도 `nlogn` 이기 한데,,,

### 실패 코드

📌[참고 코드]()

```python
# 2470 두 용액

# 합쳐서 0에 가까운 두 용액을 출력

import sys
import math
import heapq

input = sys.stdin.readline
n = int(input())
solution = [int(i) for i in input().split()]

solution.sort()
minus = 0
plus = len(solution) - 1
close_zero = math.inf
ans_minus = 0
ans_plus = 0

while True:
    temp = solution[plus] + solution[minus]
    if abs(close_zero) > abs(temp):
        close_zero = temp
        ans_minus = minus
        ans_plus = plus
        if temp == 0:
            break
    # print(solution[minus], solution[plus], temp)
    if minus >= plus:
        break

    if temp < 0:
        minus += 1
    else:
        plus -= 1
print(solution[ans_minus], solution[ans_plus])

```

위 참고 코드 링크를 통해서 고쳤는데 <br>
고친 부분 -> 하나의 - 용액을 기준으로 모든 + 용액을 비교한느게 아니라( `while solution[plus] >= 0:` ) 두 용액의 함이 음수면 - 용액의 인덱스를 1 더하고, 양수면 + 용액의 인덱스를 1 뺀다. <br>

`맞았습니다(24%)` ,,, 왜지 <br>

1. 첫 번째 `if abs(close_zero) > abs(temp):` 에서 수정이 된 - 용액의 인덱스와 + 용액의 인덱스가

```python
if temp < 0:
    minus += 1
else:
    plus -= 1
```

에서 변경이 됨. -> 해당 값을 final 리스트에 넣어주어서 값을 저장시킴. 2. 두 번째 `while True:` -> `while minus < plus:` 로 바꾸었더니 맞음이 떴는데... 이거는 왜 그런지 정확히는 모르겠음. 왜냐면 while True 일 때는 종료조건을 넣었기 때문에ㅡ,,,ㅡㅡ

### 풀이 코드

```python
# 2470 두 용액

# 합쳐서 0에 가까운 두 용액을 출력

import sys

input = sys.stdin.readline
n = int(input())
solution = [int(i) for i in input().split()]

solution.sort()
minus = 0
plus = len(solution) - 1
close_zero = abs(solution[minus] + solution[plus])
final = [solution[minus], solution[plus]]

while minus < plus:
    minus_val = solution[minus]
    plus_val = solution[plus]

    sum = minus_val + plus_val

    # - 용액과 + 용액의 합의 절대값이 기존보다 작다면 -> 값 update
    if close_zero > abs(sum):
        close_zero = abs(sum)
        final = [minus_val, plus_val]
        if sum == 0:
            break

    # - 용액을 기준으로 모든 + 용액을 검사하는게 아니라 정렬을 시켜놓은 것을 활용해서 두 용액의 합이 음수가 나오면 - 용액 인덱스를 하나 더하고, 두 용액의 합이 양수가 나오면 + 용액 인덱스를 하나 줄인다.
    if sum < 0:
        minus += 1
    else:
        plus -= 1

print(final[0], final[1])

```

### 코드 설명

`- 용액` 을 기준으로 모든 `+ 용액` 을 검사하는게 아니라 정렬을 시켜놓은 것을 활용해서 두 용액의 합이 음수가 나오면 - 용액 인덱스를 하나 더하고, 두 용액의 합이 양수가 나오면 + 용액 인덱스를 하나 줄인다. -> 이렇게 함으로써 반복문 하나를 줄여 복잡도는 O(nlogn) 이다.
