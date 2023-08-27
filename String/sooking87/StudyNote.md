## 백준 17413 단어 뒤집기 2

📌 [백준 17413 문제 링크](https://www.acmicpc.net/problem/17413) <br>

<로 시작해서 >로 끝나는 문자열은 안 뒤집고, 그 외의 문자열만 뒤집는 프로그램

### 풀이 코드

```python
# 17413 단어 뒤집기 2

# <로 시작해서 >로 끝나는 문자열은 안 뒤집고, 그 외의 문자열만 뒤집는 프로그램

import sys

input = sys.stdin.readline
string = list(input().rstrip())
result = ''
while len(string) != 0:
    if string[0] == '<':
        while len(string) != 0 and string[0] != '>':
            s = string.pop(0)
            result += s
        result += string.pop(0)
    else:
        temp = ''
        while len(string) != 0:
            # print(temp)
            if string[0] == '<':
                break
            s = string.pop(0)
            if s == ' ':
                temp += ' '
                if string[0].isalnum():
                    break
            temp = s + temp

        result += temp
print(result)
```

### 코드 설명

규칙에 맞게 풀면 되는 문제.

## 백준 17609 회문

📌 [백준 17609 문제 링크](https://www.acmicpc.net/problem/17609) <br>

회문이면 0 출력, 유사회문이면 1 출력, 그 외 2 출력

### 실패 코드

```python
# 17609 회문

# 회문이면 0 출력, 유사회문이면 1 출력, 그 외 2 출력

import sys

input = sys.stdin.readline
n = int(input())
for _ in range(n):
    string = list(input().strip())
    length = len(string) // 2
    start = 0
    end = len(string) - 1
    is_possible = False # 회문인지 아닌지를 판별
    cnt = 0 # 유사회문인지 아닌지를 판별
    for i in range(length):
        if string[start] == string[end]:
            is_possible = True
            start += 1
            end -= 1
            continue
        else:
            is_possible = False
            if string[start+1] == string[end] or string[start] == string[end-1]:
                cnt += 1
                is_possible = True
            break

    if is_possible == True and cnt == 0:
        print(0)
    elif is_possible == True and cnt == 1:
        print(1)
    else:
        print(2)
```

`정답(1%)` ,, 뭐가 문제,,,? 시간이 너무 오래걸리나?

### 실패 코드

```python
# 17609 회문

# 회문이면 0 출력, 유사회문이면 1 출력, 그 외 2 출력

import sys

input = sys.stdin.readline
n = int(input())
for _ in range(n):
    string = list(input().strip())
    length = len(string) // 2
    start = 0
    end = len(string) - 1
    is_possible = False # 회문인지 아닌지를 판별
    cnt = 0 # 유사회문인지 아닌지를 판별
    while start < end:
        print(string[start], string[end])
        if string[start] == string[end]:
            is_possible = True
        else:
            if start+1 <= length:
                if string[start+1] == string[end]:
                    start += 1
                    cnt += 1
                    is_possible = True
                elif string[start] == string[end-1]:
                    end -= 1
                    cnt += 1
                    is_possible = True

                else:
                    is_possible = False
            if not is_possible:
                break

        start += 1
        end -= 1

    if is_possible == True and cnt == 0:
        print(0)
    elif is_possible == True and cnt == 1:
        print(1)
    else:
        print(2)
```

반례

```txt
1
abca
```

start와 end 인덱스가 같아지면서 생기는 문제

### 풀이 코드

```python
# 17609 회문

# 회문이면 0 출력, 유사회문이면 1 출력, 그 외 2 출력

import sys

input = sys.stdin.readline
n = int(input())
for _ in range(n):
    string = input().strip()
    length = len(string) // 2
    start = 0
    end = len(string) - 1
    is_possible = False # 회문인지 아닌지를 판별
    while start < end:
        # 회문이라면
        if string[start] == string[end]:
            start += 1
            end -= 1
            is_possible = True
        # 유사회문 또는 회문이 아니라면
        else:
            is_possible = False
            if start <= end-1:
                temp = string[:end] + string[end+1:]
                if temp[:] == temp[::-1]:
                    print(1)
                    break
            if start+1 < end:
                temp = string[:start] + string[start+1:]
                if temp[:] == temp[::-1]:
                    print(1)
                    break
            print(2)
            break
    if is_possible:
        print(0)

```

### 코드 설명

회문이 아닌 경우 유사 회문을 찾기 위해서는 해당 인덱스(start든 end든)를 뺀 문자열을 생성해서 그게 회문이 되는지 아닌지를 판별한다. -> 문자 하나를 뺐는데도 회문이 되지 않는다면 그냥 회문이 될 수 없는 문자열이므로 2 출력하고 끝냄.

## 백준 12904 A와 B

📌 [백준 12904 문제 링크](https://www.acmicpc.net/problem/12904) <br>

문자열의 뒤에 A를 추가, 문자열을 뒤집고 뒤에 B를 추가 -> 위 규칙을 통해서 s를 t로 바꿀 수 있으면 1, 없으면 0을 출력

### 실패 코드

```python
# 12904 A와 B

# 문자열의 뒤에 A를 추가, 문자열을 뒤집고 뒤에 B를 추가
# 위 규칙을 통해서 s를 t로 바꿀 수 있으면 1, 없으면 0을 출력

import sys

input = sys.stdin.readline
s = input().rstrip()
t = input().rstrip()
# B -> BA -> ABB -> ABBA
# AB -> ABA -> ABAB
# A -> AB -> ABA -> ABAB
while len(s) != len(t):
    # B로 끝나면 뒤에 A만 추가
    if s[-1] == 'B':
        s += 'A'
    # A로 끝나면 뒤집고 B로 추가
    elif s[-1] == 'A':
        s = s[::-1] + 'B'
    print(s)

if s == t:
    print(1)
else:
    print(0)
```

마지막이 B로 끝나면 뒤에 A추가, A로 끝나면 뒤집고 B로 추가 -> 왜 틀림?

### 풀이 코드

```python
# 12904 A와 B

# 문자열의 뒤에 A를 추가, 문자열을 뒤집고 뒤에 B를 추가
# 위 규칙을 통해서 s를 t로 바꿀 수 있으면 1, 없으면 0을 출력

import sys

input = sys.stdin.readline
s = list(input().rstrip())
t = list(input().rstrip())
# B -> BA -> ABB -> ABBA
# AB -> ABA -> ABAB
# A -> AB -> ABA -> ABAB
while len(s) != len(t):
    # t에서 s로 가려면 A를 제거
    if t[-1] == 'A':
        t.pop()
    # t에서 s로 가려면 B가 제거되고 뒤집어야됨
    elif t[-1] == 'B':
        t.pop()
        t = t[::-1]
    # print(t)

if s == t:
    print(1)
else:
    print(0)

```

왜 틀렸냐면 사실 문제에는 어떤 경우에 A가 추가되고, 어떤 경우에 뒤집고 B가 추가되는지가 나와있ㅈㅣ 않는다. 결국, T에서 S로 유추를 하는 방법밖에 없다.

### 코드 설명

문제에서는 S -> T가 될 수 있다면 1을 출력, 아니라면 0을 출력하도록 나와있는데 <br>

결국 T -> S로 역추적하면서 S가 되는지를 봐야되는 문제 왜냐하면 어떠한 경우에 A가 추가되고, 어떤 경우에 뒤집고 B가 추가되는지를 모르기 때문에!

## 백준 9342 염색체

📌 [백준 9342 문제 링크](https://www.acmicpc.net/problem/9342) <br>
A가 하나 또는 그 이상, F가 하나 또는 그 이상, C가 하나 또는 그 이상, {A, B, C, D, E, F} 중 0개 또는 1개가 있으며, 더 이상의 문자는 없어야 한다.

### 풀이 코드

```python
# 9342 염색체

# A가 하나 또는 그 이상, F가 하나 또는 그 이상, C가 하나 또는 그 이상, {A, B, C, D, E, F} 중 0개 또는 1개가 있으며, 더 이상의 문자는 없어야 한다.

import sys
import re

input = sys.stdin.readline
n = int(input())
# ^ 해당 패턴으로 시작
# ? 해당 패턴을 0번 또는 1번
# $ 해당 패턴으로 끝
# + 해당 패턴이 하나 이상
comp = re.compile('^[A-F]?A+F+C+[A-F]?$')
for _ in range(n):
    print('Good' if comp.match(input()) == None else 'Infected!')
```

### 코드 설명

정규 표현식 re를 사용해서 문제를 푸는 문제였다.
