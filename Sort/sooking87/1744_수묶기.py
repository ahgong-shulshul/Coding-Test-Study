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
