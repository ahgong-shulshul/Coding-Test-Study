# 20164 홀수 홀릭 호석

# 숫자 개수가 1개 -> 그대로 출력
# 숫자 개수가 2개 -> 두 수를 더함
# 숫자 개수가 3개 이상 -> 임의의 지점에서 세 수를 나누어 더함
# 나올 수 있는 홀수의 최댓값과 최솟값을 구하는 문제

# 514(2) -> 5 + 1 + 4 = 10(1) -> 1(1)

# 쪼개진 상태로 그 값을 유지하면서 사용해야되므로 재귀를 사용해야될 것 같음.

import math


def odd_counting(n):
    odd_cnt = 0
    for i in n:
        if int(i) % 2 != 0:
            odd_cnt += 1
    return odd_cnt


def main_func(n, odd_cnt):
    global min_v, max_v

    if len(n) == 1:
        min_v = min(min_v, odd_cnt)
        max_v = max(max_v, odd_cnt)
    elif len(n) == 2:
        first = int(n[0])
        second = int(n[1])
        temp = str(first + second)
        main_func(temp, odd_cnt + odd_counting(temp))
    else:
        for i in range(1, len(n) - 1):
            for j in range(i + 1, len(n)):
                first = int(n[0:i])
                second = int(n[i:j])
                last = int(n[j:len(n)])
                temp = str(first + second + last)
                main_func(temp, odd_cnt + odd_counting(temp))


n = input()
min_v = math.inf
max_v = 0

main_func(n, odd_counting(n))
print(min_v, max_v)
