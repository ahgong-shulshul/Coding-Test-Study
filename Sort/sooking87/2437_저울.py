# 2437 저울

# 입력받은 무게추들 중에서 측정할 수 없는 양의 정수 무게 중 최솟값을 구하기

import sys
import itertools as it

input = sys.stdin.readline
n = int(input())
weight = [int(i) for i in input().split()]
weight.sort()

target = 1
# w를 더하다가 target보다 크게되면 그 다음 숫자부터는 만들 수 없는 추 무게가 된다...
for w in weight:
    if target < w:
        break  
    target += w
print(target)