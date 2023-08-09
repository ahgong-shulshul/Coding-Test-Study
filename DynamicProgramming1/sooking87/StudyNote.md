
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
