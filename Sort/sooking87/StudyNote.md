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



## 백준 1744 수 묶기

📌 [백준 1744 문제 링크](https://www.acmicpc.net/problem/1744) <br>
입력 받은 수를 단 한 번 또는 0번 묶어서 최대 수 출력하기

### 실패 코드

```python
# 1744 수 묶기

# 입력 받은 수를 단 한 번 또는 0번 묶어서 최대 수 출력하기

import sys

input = sys.stdin.readline
n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))

nums.sort(reverse = True)

ans = 0
i = 0
is_last = False
while i < n - 1:
    temp1 = nums[i] * nums[i + 1]
    temp2 = nums[i] + nums[i + 1]
    if temp1 < temp2:
        ans += nums[i]
        is_last = False
    else:
        ans += temp1
        i += 1
        is_last = True
    i += 1
if not is_last:
    ans += nums[-1]
print(ans)
```

예제 코드는 다 맞았는데 `채점 중(5%)` ,,, <br>

뭐지 뭐가 문제지? <br>
질문 게시판의 반례를 찾아보니까
```txt
3
1
2
3
```
의 값은 7이 나와야되는데 6이 나옴...

### 실패 코드

위의 반례가 맞을 수 있도록 (원인: is_last를 통해서 마지막에 더해야되는지 말아야되는지 판단 한 것) 코드를 수정했다. 

```py
# 1744 수 묶기

# 입력 받은 수를 단 한 번 또는 0번 묶어서 최대 수 출력하기

import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))

nums.sort(reverse = True)
queue = deque(nums)

ans = 0
i = 0
is_last = False
num1 = queue.popleft()
while queue:
    num2 = queue.popleft()
    # print(num1, num2)
    temp1 = num1 * num2
    temp2 = num1 + num2
    if temp1 < temp2:
        ans += num1
        num1 = num2
    else:
        ans += temp1
        num1 = queue.popleft()
    # print(ans)
if not is_last:
    ans += nums[-1]
print(ans)
```

큐를 사용해서 큐가 빌 때까지 위 과정을 반복하는 것이다. -> `런타임 에러(IndexError),,` <br>

else문에 있는 popleft() 때문에 생긴다. 사실 queue가 비어있으면 그 상태로 종료를 해야되므로 해당 부분 코드 수정 완료

### 실패 코드

```python
# 1744 수 묶기

# 입력 받은 수를 단 한 번 또는 0번 묶어서 최대 수 출력하기

import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))

nums.sort(reverse = True)
queue = deque(nums)
# print(queue)

ans = 0
num1 = queue.popleft()
while queue:
    num2 = queue.popleft()
    # print(num1, num2)
    # print(queue)
    temp1 = num1 * num2
    temp2 = num1 + num2
    if temp1 < temp2:
        ans += num1
        num1 = num2
    else:
        ans += temp1
        if queue:
            num1 = queue.popleft()
    # print(ans)

print(ans)
```

음,,, 바로 `틀렸습니다` 로 뜸,,,, 왜? <br>

```txt
5
-1
-2
-3
-4
-5

ans = 25
```
반례 발견 -> 양수는 내림차순 정렬, 음수는 오름차순 정렬로 해보면 어떨까? / 음수만 짝수개 있으면 상관이 없는데 홀수개로 있는 경우가 문제.

### 풀이 코드

```python
# 1744 수 묶기

# 입력 받은 수를 단 한 번 또는 0번 묶어서 최대 수 출력하기

import sys

input = sys.stdin.readline
n = int(input())
pos = []
neg = []
ans = 0
for _ in range(n):
    num = int(input())
    if num > 1:
        pos.append(num)
    elif num == 1:
        ans += 1 # 1 1 이렇게 입력이 된다면 밑에서는 무조건 곱하면서 더해지기 때문에 1이 입력되는 경우는 그냥 더해주면 된다.
    else:
        neg.append(num)

pos.sort(reverse=True) # 양수는 내림차순 정렬
neg.sort() # 음수는 오름차순 정렬

# 양수 더하기
if len(pos) % 2 == 0:
    for i in range(0, len(pos), 2):
        ans += pos[i] * pos[i + 1]
else:
    for i in range(0, len(pos) - 1, 2):
        ans += pos[i] * pos[i + 1]
    ans += pos[-1]

# 음수 더하기
if len(neg) % 2 == 0:
    for i in range(0, len(neg), 2):
        ans += neg[i] * neg[i + 1]
else:
    for i in range(0, len(neg) - 1, 2):
        ans += neg[i] * neg[i + 1]
    ans += neg[-1]

print(ans)

```
결국 음수, 양수를 나누고 그냥 규칙대로 곱해주면 됨. 그리고 1을 따로 뺀 이유는 밑에 반복문에서는 무조건 *를 통해서 더할 것이기 때문에 + 1의 경우는 양수든 음수든 무조건 (1 + 음수/양수) 라는 숫자가 차피 더 크다. 1은 곱했을 때 자기 자신을 결과로 내기 때문에 `1` 이라는 숫자를 조금 특이하게 생각했어야 된다. <br>

대부분의 숫자 곱이 덧셈보다 크기 때문에 이를 이용해서 반복문에 *만 넣을 생각을 했어야 됐고, 여기서 1이라는 숫자만 반례가 있다는 것을 인지했어야 됐다.

### 코드 설명

양수랑 음수를 나누었기 때문에 굳이 +, *를 비교할 필요없이 무조건 곱해주면서 더해주면 됨.