# 9342 염색체

# A가 하나 또는 그 이상, F가 하나 또는 그 이상, C가 하나 또는 그 이상, {A, B, C, D, E, F} 중 0개 또는 1개가 있으며, 더 이상의 문자는 없어야 한다.

import sys
import re

input = sys.stdin.readline
n = int(input())
# ^ 해당 패턴으로 시작
# ? 해당 패턴을 0번 또는 1번
# $ 해당 패턴으로 끝
# + 해당 패턴이 하나 이상
comp = re.compile('^[A-F]?A+F+C+[A-F]?$')
for _ in range(n):
    print('Good' if comp.match(input()) == None else 'Infected!')
