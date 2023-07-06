# 21314 민겸 수
# Silver2
# Greedy 알고리즘
# 풀이 날짜: 2023-07-04

# 풀이 전략
# 가장 큰 수: 문자열에서 K로 끝날 때마다 문자열을 쪼갬
# 가장 작은 수: 가장 큰 수에서 K를 M과 분리(붙어있는 M제외 모든 문자열을 자르기)

# !답은 나오지만 백준 채점 시 Overflow Error 발생!
import math

num = input()

min_num = ""
max_num = ""

cnt = 0
for i in range(len(num)):
    temp1 = 1
    if (num[i] == "M"):
        cnt += 1
    if (num[i] == "K"):
        temp1 = int(5 * math.pow(10, cnt))
        max_num += str(temp1)
        cnt = 0
if (cnt != 0):
    max_num = max_num + "1" * cnt

cnt = 0
for i in range(len(num)):
    temp1 = 1
    if (num[i] == "M"):
        cnt += 1
    if (num[i] == "K"):
        temp1 = int(math.pow(10, cnt - 1))
        if (temp1 != 0):
            min_num = min_num + str(temp1) + "5"
        else:
            min_num += "5"
        cnt = 0
if (cnt != 0):
    min_num += str(int(math.pow(10, cnt - 1)))

print(max_num)
print(min_num)
