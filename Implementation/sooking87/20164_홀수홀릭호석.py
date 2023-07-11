# 20164 홀수 홀릭 호석

# 숫자 개수가 1개 -> 그대로 출력
# 숫자 개수가 2개 -> 두 수를 더함
# 숫자 개수가 3개 이상 -> 임의의 지점에서 세 수를 나누어 더함
# 나올 수 있는 홀수의 최댓값과 최솟값을 구하는 문제

# 514(2) -> 5 + 1 + 4 = 10(1) -> 1(1)

import sys
import itertools as it

input = sys.stdin.readline
n = input()
# 문자열 입력 시 \n 제거
n = n.replace('\n', '')
print(n[0:1])
ans = n
while True:
    if len(n) == 1:
        break
    elif len(n) == 2:
        ans = int(n[0]) + int(n[1])
    else:
        print('3이상인 경우')
        for i in range(len(n) - 1):
            for j in range(i + 1, len(n)):
                print(n[0:i])
