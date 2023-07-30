# 1263 시간관리
# Gold5
# 정렬 알고리즘
# 풀이 날짜: 2023-07-27


n = int(input())

load = []
temp = []
for i in range(n):
    temp = [int(m) for m in input().split()]
    load.append(temp)

load.sort(key=lambda x: (-x[1], -x[0]))
# print(load)

time = load[0][1]
temp = 0
idx = 0
while(time > 0 and idx < n):
    temp = time - load[idx][0]
    if (idx == n - 1):
        time = temp
        break
    elif (temp > load[idx + 1][1]):
        time = load[idx + 1][1]
    else:
        time = temp
    idx += 1

if (time >= 0):
    print(time)
else:
    print(-1)