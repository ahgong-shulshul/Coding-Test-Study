# 16935 A->B

# 정수 A를 B로 바꾸려고 한다. 
# 2를 곱하거나 1을 수의 가장 오른쪽에 추가한다. 두 가지 연산 중 연산의 최소값을 구해보자

import sys

input = sys.stdin.readline
a, b = map(int, input().split())
cnt = 0

while b > a:
    if b % 2 == 0:
        b //= 2

    elif (b % 10 != 0) and (int(str(b)[-1]) == 1):
        b //= 10
    cnt += 1

    if (int(str(b)[-1]) != 1) and (b % 2 != 0):
        break
    
if a == b:
    print(cnt + 1)
else:
    print(-1)