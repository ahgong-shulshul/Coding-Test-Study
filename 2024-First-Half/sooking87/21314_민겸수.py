# 21314 민겸수

# 10**n꼴의 십진수는 M이 N+1개
# 5*10**n꼴이면 n개의 m 뒤에 1개의 k를 이어붙히기

import sys

input = sys.stdin.readline
word = input().rstrip()
# MKKMMK -> 505500 / 155105
# K = 5 / M = 10
max = ''
min = ''
# 최소가 되려면 M 연속이면 M-1 개수만큼 0을 붙힌다
# 최소가 되려면 K가 나올때마다 끊어야됨
# 최대가 되려면 M 연속이면 K까지에서 끊어야됨
temp = 0
for i in word:
    if i == 'M':
        temp += 1
    else:
        if temp > 0:
            max += str(5 * (10**temp))
            min += str(10**temp + 5)
        else:
            max += '5'
            min += '5'
        temp = 0
        
# 'M'으로 끝날 경우
if temp>0:
    max += '1'*temp
    min += str(10**(temp-1))
print(max)
print(min)
