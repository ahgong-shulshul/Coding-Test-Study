# 19637 IF문 좀 대신 써줘
# Silver2
# 이진탐색
# 풀이 날짜: 2023-08-02


def binary_search(status, target):
    low = 0
    high = len(status) - 1
    mid = 0
    result = 0
    while(low <= high):
        mid = (low + high) // 2
        if (status[mid][1] >= target):
            high = mid - 1
            result = mid
        elif (status[mid][1] < target):
            low = mid + 1

    print(status[result][0])

n, m = map(int, input().split())

status = []
for i in range(n):
    temp = []
    s, pow = input().split()
    temp.append(s)
    temp.append(int(pow))
    status.append(temp)

power = []
for i in range(m):
    power.append(int(input()))

for i in range(m):
    binary_search(status, power[i])



"""
idx = 0
while (idx < m):
    if (power[idx] <= status[0][1]):
        print(status[0][0])
    elif(power[idx] <= status[1][1]):
        print(status[1][0])
    elif(power[idx] <= status[2][1]):
        print(status[2][0])
    idx += 1
"""