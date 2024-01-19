# 1744 수 묶기
# Gold4
# 정렬 알고리즘
# 풀이 날짜: 2023-07-28

# 풀이 전략
# 음수 배열, 양수배열로 나눔, 따로 계산
# 0 있느냐 없느냐만 중요 -> 음수가 홀수일 때 하나 남은 음수를 0으로 상쇄시켜줌


n = int(input())

plus = []
minus = []
zero = False
for _ in range(n):
    temp = int(input())
    if (temp > 0):
        plus.append(temp)
    elif (temp < 0):
        minus.append(temp)
    else:
        zero = True

plus.sort(reverse=True)
minus.sort()

sum = 0
idx = 0
while (idx < len(plus) - 1):
    temp_mul = plus[idx] * plus[idx + 1]
    temp_add = plus[idx] + plus[idx + 1]
    if (temp_mul > temp_add):
        sum += temp_mul
    else:
        sum += temp_add
    idx += 2
if (len(plus) % 2 != 0):
    sum += plus[-1]

idx = 0
while (idx < len(minus) - 1):
    sum += minus[idx] * minus[idx + 1]
    idx += 2
if (len(minus) % 2 != 0 and zero == False):
    sum += minus[-1]

print(sum)
