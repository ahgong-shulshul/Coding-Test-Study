# 1920 수 찾기

# 정수 n개 중 x라는 정수가 존재하는지 알아내는 프로그램

import sys

input = sys.stdin.readline
n = int(input())
a = [int(i) for i in input().split()]
a.sort()
m = int(input())
is_in_a = [int(i) for i in input().split()]

for i in range(m):
    is_possible = False
    compare = is_in_a[i]
    start_idx = 0
    end_idx = n - 1
    while start_idx <= end_idx:
        mid_idx = (start_idx + end_idx) // 2
        if compare == a[mid_idx]:
            print(1)
            is_possible = True
            break
        if compare > a[mid_idx]:
            start_idx = mid_idx + 1
        else:
            end_idx = mid_idx - 1
    if not is_possible:
        print(0)