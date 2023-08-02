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