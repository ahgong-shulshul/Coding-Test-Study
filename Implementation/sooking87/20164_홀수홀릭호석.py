# 20164 홀수 홀릭 호석

# 숫자 개수가 1개 -> 그대로 출력
# 숫자 개수가 2개 -> 두 수를 더함
# 숫자 개수가 3개 이상 -> 임의의 지점에서 세 수를 나누어 더함
# 나올 수 있는 홀수의 최댓값과 최솟값을 구하는 문제

# 514(2) -> 5 + 1 + 4 = 10(1) -> 1(1)

# 쪼개진 상태로 그 값을 유지하면서 사용해야되므로 재귀 사용.

import sys
import math
import copy

def split_three(n):
    for i in range(1, len(copy_n) - 1):
        for j in range(i + 1, len(copy_n)):
            first = int(copy_n[0:i])
            second = int(copy_n[i:j])
            last = int(copy_n[j:len(copy_n)])
            copy_n = str(first + second + last)
            print(first, second, last)
            print(copy_n)


input = sys.stdin.readline
n = input()
# 문자열 입력 시 \n 제거
n = n.replace('\n', '')
ans = n
cnt = 0
cnt_list = []
loop = math.comb(len(n) - 1, 2) # 몇 개를 쪼갤 수 있는지
print(loop)
for _ in range(loop):
    copy_n = n
    while True:
        print('----------')
        if int(copy_n) % 2 != 0:
            cnt += 1
            print('cnt', cnt)
        
        if len(copy_n) == 1:
            break
        elif len(copy_n) == 2:
            print("2인 경우", copy_n)
            first = int(copy_n[0])
            second = int(copy_n[1])
            if first % 2 != 0:
                cnt += 1
            if second % 2 != 0:
                cnt += 1
            copy_n = str(first + second)
        else:
            print('3이상인 경우')
            for i in range(1, len(copy_n) - 1):
                for j in range(i + 1, len(copy_n)):
                    first = int(copy_n[0:i])
                    second = int(copy_n[i:j])
                    last = int(copy_n[j:len(copy_n)])
                    copy_n = str(first + second + last)
                    print(first, second, last)
                    print(copy_n)
                    if first % 2 != 0:
                        cnt += 1
                    if second % 2 != 0:
                        cnt += 1
                    if last % 2 != 0:
                        cnt += 1
                    print('end')
                print('*')
            print(copy_n)
    cnt_list.append(cnt)
print('cnt', cnt_list)
