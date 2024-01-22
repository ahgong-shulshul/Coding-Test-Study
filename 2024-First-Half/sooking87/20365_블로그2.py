# 20365 블로그 2

# 풀어야되는 문제수 n, r은 빨간색, b는 파란색으로 칠한다.

import sys

input = sys.stdin.readline
n = int(input())
colors = list(input())[:-1]
cnt_list = []
cnt1 = 0
cnt2 = 0
cnt3 = 0

# 한 번에 파란색을 칠하고 빨간색만 추가적으로 칠하는 경우 + 바뀌기 전까지만 한 번에 칠하기 -> 반드시 파란색으로 덮는 것이 아니라 빨간색으로 덮고 파란색을 덫칠하는 경우도 생각

# 전체 파란칠 + R만 위에 덫칠
for i in range(len(colors)-1):
    if colors[i]=='B' and colors[i+1]=='R':
        cnt1 += 1
    if colors[0] == 'R':
        cnt1 += 1
cnt_list.append(cnt1+1)

# 전체 빨간칠 + B만 위에 덫칠
for i in range(len(colors)-1):
    if colors[i] == 'R' and colors[i+1] == 'B':
        cnt2 += 1
    if colors[0] == 'B':
        cnt2 += 1
cnt_list.append(cnt2+1)

# 해당 색깔별로 각각 칠하기
for i in range(len(colors)-1):
    if colors[i] != colors[i+1]:
        cnt3 += 1
cnt_list.append(cnt3+1)

# print(cnt_list)
print(min(cnt_list))