# 19583 싸이버 개강총회
# Silver2
# String
# 풀이 날짜: 2023-08-27


import sys
input = sys.stdin.readline


start, end, q = input().split(" ")

std = []
while(True):
    t, name = input().split(" ")
    if t <= start:
        std.append(name)
    if t > start:
        last_time, last_name = t, name
        break

cnt = 0
count = []
if end <= last_time <= q and last_name in std:
    cnt += 1

while (True):
    try:
        t, name = input().split(" ")
        if end <= t <= q and name in std and name not in count:
            count.append(name)
            cnt += 1
        if t > q:
            break
    except:
        break
    

print(cnt)
