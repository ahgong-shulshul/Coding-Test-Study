# 2669 숫자고르기

# 첫 째줄과 둘 째줄에서 집합으로 겹치는 최대 개수랑, 숫자를 출력

# BFS, DFS를 어떤 식으로 사용하려나?
# https://velog.io/@deannn/BOJ-%EB%B0%B1%EC%A4%80-2668%EB%B2%88-%EC%88%AB%EC%9E%90%EA%B3%A0%EB%A5%B4%EA%B8%B0-Python
# 근데 왜 이코드가 dfs이지? -> 재귀 사용

import sys
from collections import deque

def make_set(first_line, second_line, num):
    first_line.add(num)
    second_line.add(arr[num])
    
    if arr[num] in first_line:
        if first_line == second_line: # 첫 째줄 집합과 둘 째줄 집합이 같다면
            ans.update(first_line)
            return True
        return False
    return make_set(first_line, second_line, arr[num])

input = sys.stdin.readline
n = int(input())
arr = [0]
for _ in range(n):
    arr.append(int(input()))

ans = set()
for i in range(1, n + 1):
    if i not in ans:
        make_set(set(), set(), i)

print(len(ans))
print(*sorted(list(ans)), sep = '\n')