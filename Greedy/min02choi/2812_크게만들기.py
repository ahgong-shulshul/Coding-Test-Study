# 2812 크게 만들기
# Gold3
# Greedy 알고리즘
# 풀이 날짜: 2023-07-09

import time

n, k = map(int, input().split())
num = input()

start = time.time()

# 인덱스 0~k까지의 숫자를 배열에 저장
can = [num[i] for i in range(k + 1)]
# print(can)

idx = can.index(max(can))       # 가장 큰 수의 인덱스 탐색
k -= idx
# print(idx)
first = max(can)

num = num[idx:]     # 원본 숫자에서 앞부분 떼어내기

can = [num[i] for i in range(1, len(num))]
nn = 0

while(len(can)):
    cnt = 0
    for i in can:
        if (i != ""):
            cnt += 1

    if (k == 0 or nn == cnt):
        break

    temp = sorted(can, reverse=True)

    max_num = temp[nn]
    for j in range(can.index(max_num, nn)):

        sub_str = sorted(can[0:can.index(max_num, nn)])

        if (sub_str[j] < max_num and k > 0 and sub_str[j] != ""):
            n_idx = can.index(sub_str[j])
            can[n_idx] = ""
            k -= 1
    nn += 1

print(can)
print(num)

if (k > 0):
    can = can[0:len(can) - k]

string = ""
for i in can:
    string += i
print(first + string)

end = time.time()
print(end - start)