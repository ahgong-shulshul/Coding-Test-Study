# 2812 크게 만들기
# Gold3
# Greedy 알고리즘
# 풀이 날짜: 2023-07-09

# 답은 나오는데 시간초과 뜸. 아마 다른테스트 케이스에 대한 무한루프..

import time


n, k = map(int, input().split())
num = input()

start = time.time()

# 인덱스 0~k까지의 숫자를 배열에 저장
can = [num[i] for i in range(k)]
# print(can)

idx = can.index(max(can))       # 가장 큰 수의 인덱스 탐색
k -= idx
# print(idx)
first = max(can)

num = num[idx:]     # 원본 숫자에서 앞부분 떼어내기
# print(num)

while(k > 0):
    can = [num[i] for i in range(1, len(num))]
    max_num = max(can)
    for j in range(can.index(max_num)):

        sub_str = sorted(can[0:can.index(max_num)])

        if (sub_str[j] < max_num and k > 0):
            n_idx = can.index(sub_str[j])
            can[n_idx] = ""
            k -= 1

print(can)
print(num)

string = ""
for i in can:
    string += i
print(first + string)

end = time.time()
print(end - start)