# 1541 잃어버린 괄호

# 입력받은 수식에서 괄호를 쳐서 최소의 값을 구하는 문제
import sys
from collections import deque

input = sys.stdin.readline
expression = input()

sp_minus = expression.split('-')
sum = 0
# - 앞쪽 부분은 무조건 + 일 것 이므로 모두 더해준다.
for i in sp_minus[0].split('+'):
    sum += int(i)

for i in sp_minus[1:]:
    # - 이후에 + 가 있다면 걔는 - 로 바꾸어주면 괄호를 친 격이 된다(-( + + ) == - - ) 괄호 풀면 -로 바뀜
    for j in i.split('+'):
        sum -= int(j)
print(sum)