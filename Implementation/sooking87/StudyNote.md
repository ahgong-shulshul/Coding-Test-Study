## 완전 탐색

컴퓨터의 빠른 계산 성능을 활용하여 가능한 모든 경우의 수를 탐색하는 방법 == *무식하게 푼다* 의 의미인 **Brute Force**  라고도 부름 <br>
문제에서 주어질 수 있는 모든 경우의 수를 탐색하는 알고리즘

### 완전 탐색 방법

📌 [완전 탐색 풀이법 참고 링크](https://velog.io/@sxbxn/%EC%99%84%EC%A0%84%ED%83%90%EC%83%89) <br>

1. 해결하고자 하는 문제의 가능한 경우의 수를 대략적으로 계산
2. 가능한 모든 방법을 다 고려 -> 여기에는 단순 Brute Force, 순열, 재귀 호출, 비트마스크, BFS, DFS
3. 실제 답을 구할 수 있는지 적용 <br>

- 단순 Brute Force: 반복문, 조건문을 활용하여 단순하게 모든 방법을 찾는 방법(ex. 자물쇠 암호를 찾는 경우 0000 ~ 9999 모든 경우를 확인)
- BFS, DFS 활용: 그래프 자료구조에서 모든 정점을 탐색하기 위한 방법
- 순열: 임의의 수열이 있을 때, 그것을 다른 순서로 연산하는 방법인 순열을 활용하는 방법
- 재귀 호출: 재귀 함수를 통해 해결하는 방법
- 비트마스크: 비트 연산을 통해 부분 집합을 표현하는 방법

### 완전 탐색은 언제 사용하면 좋을까?

보통 완전 탐색 문제는 for문과 if문을 활용하거나, BFS/DFS를 활용하는 경우가 대부분. <br>
+a. 순열을 활용해 완전 탐색 문제를 푸는 방법도 자주 나옴 <br>

1. 입력으로 주어지는 데이터의 크기가 매주 작을 떼(데이터의 크기가 커지게 되면 O(2^N)이나, O(N!)이므로!)
2. 답의 범위가 작고, 임의의 답을 하나 선택했을 때 문제 조건을 만족하는지 역추적할 수 있을 떼. -> ❓

### 알고리즘에서 주로 쓰는 함수

1. product(곱집합) `itertools.product('1234', repeat = 2)` <br>
    이중 for문 형식으로 생각 <br>
    ```txt
    [('1', '1'), ('1', '2'), ('1', '3'), ('1', '4'),
    ('2', '1'), ('2', '2'), ('2', '3'), ('2', '4'),
    ('3', '1'), ('3', '2'), ('3', '3'), ('3', '4'),
    ('4', '1'), ('4', '2'), ('4', '3'), ('4', '4')]
    ```
2. permutations(순열) `itertools.permutations('1234', 2)` <br>
    가능한 모든 순서를 반환, 반복되는 요소가 없다. <br>
    위의 예시로는 1234 중 2개를 순서 상관 있이 뽑는 경우의 수. 즉, <small>4</small>P<small>2</small> <br>
    ```txt
    [('1', '2'), ('1', '3'), ('1', '4'),
    ('2', '1'), ('2', '3'), ('2', '4'),
    ('3', '1'), ('3', '2'), ('3', '4'),
    ('4', '1'), ('4', '2'), ('4', '3')]
    ```
3. combinations(조합) `combinations('1234', 2)` <br>
    <small>4</small>C<small>2</small> <br>
    ```txt
    [('1', '2'), ('1', '3'), ('1', '4'),
    ('2', '3'), ('2', '4'),
    ('3', '4')]
    ```
4. combinations_with_replacement(중복이 가능한 조합) `combinations_with_replacement('1234', 2)` <br>
    조합에서 개별 요소마다 두 번이상 반복할 수 있다. <br>
    ```txt
    [('1', '1'), ('1', '2'), ('1', '3'), ('1', '4'),
    ('2', '2'), ('2', '3'), ('2', '4'),
    ('3', '3'), ('3', '4'),
    ('4', '4')]
    ```

## 백준 12933 오리

📌 [백준 12933 문제 링크](https://www.acmicpc.net/problem/12933) <br>

- quack가 문자열에서 몇 개 있는지 리턴 <br>

예제 1 해석 <br>
quqacukqauackck <br>
qu_ac_kq_uack <br>
__q__u__a____ck <br>

이렇게 되어서 출력이 2가 되는 것이다.

### 실패 코드

```python
# 12933 오리

# quack가 문자열에서 몇 개 있는지 리턴
# 문자열의 길이가 작다 -> 완전 탐색(노가다,,)

import sys
import copy

input = sys.stdin.readline
str = input()
str_list = list(str)
cnt = 0
# quqacukqauackck
duck = 'quack'
duck_idx = 0
i = 0

# quack가 끝나고 quack가 연결되어서 나오면 한 오리가 울었다고 판단
# quack가 끝나기 전에 q가 시작되면 다른 오리의 울음

#* quack 사이에 q의 개수가 리턴 개수?
while True: 
    if len(str_list) == 1: # \n은 제외
        break
    if str_list[i] == duck[duck_idx]:
        duck_idx += 1
        dele = str_list.pop(i)
        print(i, dele, str_list)
    else:
        i += 1
    if duck_idx == len(duck):
        cnt += 1
        duck_idx = 0
        i = 0
    print(cnt)
```

처음에 이렇게 풀었는데 이렇게 된다면 예제의 첫 번째 경우가 해결되지 않는다. -> 어떻게 해야 해결할 수 있을까? itertools를 사용해야되나? combination?

### 실패 코드

`시간 초과`

```python
# 12933 오리

# quack가 문자열에서 몇 개 있는지 리턴
# 문자열의 길이가 작다 -> 완전 탐색(노가다,,)

import sys
import itertools as it

input = sys.stdin.readline
str = input()
str_list = list(str)
cnt = 0
duck = 'quack'

# quack가 끝나고 quack가 연결되어서 나오면 한 오리가 울었다고 판단
# quack가 끝나기 전에 q가 시작되면 다른 오리의 울음

while True: 
    # 문자열 한 번 스캔 -> 거기서 quack이 여러번 나와도 한 마리의 오리가 낸 소리
    duck_idx = 0
    i = 0
    is_one_sound = 1 # 0: no, 1: yes
    while True:
        # 문자열 한 번 스캔을 위한 종료문
        if i == len(str_list):
            break
        # q, u, a, c, k와 같다면 str_list에서 지우기
        if str_list[i] == duck[duck_idx]:
            duck_idx += 1
            dele = str_list.pop(i)
        # 그게 아니라면 비교하기 위한 str_list의 인덱스만 증가
        else:
            i += 1
        if (duck_idx == len(duck)):
            # quack__qu_a_ck 의 경우는 한 오리가 내는 소리이므로 is_one_sound를 통해서 판단
            if is_one_sound == 1:
                cnt += 1
                is_one_sound = 0
            duck_idx = 0
    if (len(str_list) == 1) or (cnt == 0): # \n은 제외
        break
if cnt != 0:
    print(cnt)
else:
    print(-1)
```

어제 생각하던 알고리즘에서 `is_one_sound` 변수를 추가해서 보충했다. -> 근데 시간 초과,,,, <br>

+a. `quackqauckquack` 얘는 출력 안돼 근데 출력한다고 해서 1이 나올 것 같은데,,, 왜 -1이 나와야되지? <br>
질문 게시판을 보니까 `quackqua` 가 -1이 나와야되는 것을 보면 울다만 경우는 cnt 하지 않는다. <br>

`마지막에 오리가 다 울어도 그전에 울다 만 소리들이 있다면 -1이 됩니다` -> 뭔 개소리야. 그럼 뒤에서 quack가 있다고 해서 앞에 완성되지 않으면 -1? <br>

근데 예제 6은 왜 -1이야???????????????? <br>
qauck 라는 문자열이 남아있으므로,, 그렇게 되면 녹음이 덜 된 경우임.. 젼나 어렵넹 떼잉

### 풀이 코드

```python
# 12933 오리

# quack가 문자열에서 몇 개 있는지 리턴
# 문자열의 길이가 작다 -> 완전 탐색(노가다,,)

import sys
import itertools as it

input = sys.stdin.readline
str = input()
str_list = list(str)
cnt = 0
duck = 'quack'

# quack가 끝나고 quack가 연결되어서 나오면 한 오리가 울었다고 판단
# quack가 끝나기 전에 q가 시작되면 다른 오리의 울음
# 녹음한 소리가 올바르지 않은 경우에는 -1을 출력 = 반드시 str_list에 남은게 \n만 있어야됨.

while True: 
    # 소리가 제대로 녹음되지 않은 경우
    if (len(str_list) - 1) % 5 != 0:
        break
    # 문자열 한 번 스캔 -> 거기서 quack이 여러번 나와도 한 마리의 오리가 낸 소리
    duck_idx = 0
    i = 0
    is_one_sound = 1 # 0: no, 1: yes
    while True:
        # 문자열 한 번 스캔을 위한 종료문
        if i == len(str_list):
            break
        # q, u, a, c, k와 같다면 str_list에서 지우기
        if str_list[i] == duck[duck_idx]:
            duck_idx += 1
            dele = str_list.pop(i)
        # 그게 아니라면 비교하기 위한 str_list의 인덱스만 증가
        else:
            i += 1
        if (duck_idx == len(duck)):
            # quack__qu_a_ck 의 경우는 한 오리가 내는 소리이므로 is_one_sound를 통해서 판단
            if is_one_sound == 1:
                cnt += 1
                is_one_sound = 0
            duck_idx = 0
    if (len(str_list) == 1) or (cnt == 0): # cnt == 0이면 quack이 하나도 안나왔다는 뜻 -> 더이상 검사 필요 없음.
        break
if (cnt != 0) and len(str_list) == 1:
    print(cnt)
else:
    print(-1)
```

### 코드 설명

예제를 보게 되면 qu__ackq_u__a_ck 로 나와있으면 한 마리의 오리가 운 것으로 봐야됨 <br>

2중 루프를 통해서 안에 있는 while 문의 경우는 한 번 문자열을 스캔하기 위한 반복문이고, 이를 계속 반복해가면서 `quack` 를 발견하기 위한 반복문이 바깥 반복문이다. <br>

여기서 `is_one_sound` 라는 변수를 통해서 문자열 한 번을 스캔할 때, quack가 끝나고 나오는 다음 quack의 경우는 cnt를 하지 않았다. <br>

그리고 소리가 덜 녹음된 경우, 리스트에서 \n 이외의 다른 문자열이 있는 경우는 -1을 출력(마지막 조건문) <br>

근데 이런게 Implementation 인건가,,?
