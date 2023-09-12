# 호텔 구조 -> 완전 이진 트리
# 가장 꼭대기 층이 1층, 아래로 내려올수록 층의 번호가 1씩 증가
import sys

def get_roomnum(num):
    exponents = 0
    first_num = 0
    copy_num = num
    while True:
        if copy_num - 2 ** exponents > 0:
            first_num += 1
            copy_num -= 2 ** exponents
            exponents += 1
        else:
            break
    first_num += 1
    last_num = (num - 2 ** exponents) + 1
    if len(str(last_num)) < 18:
        roomnum = str(first_num)
        roomnum += str(last_num).rjust(18, '0')
    else:
        roomnum = str(first_num) + str(last_num)
    return int(roomnum)

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    now = int(input())
    print(get_roomnum(now))
    while now != 1:
        if now % 2 == 0:
            now //= 2
        else:
            now = (now - 1) // 2
        ans = get_roomnum(now)
        print(ans)