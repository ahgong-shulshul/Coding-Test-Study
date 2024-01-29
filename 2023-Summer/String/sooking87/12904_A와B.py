# 12904 A와 B

# 문자열의 뒤에 A를 추가, 문자열을 뒤집고 뒤에 B를 추가
# 위 규칙을 통해서 s를 t로 바꿀 수 있으면 1, 없으면 0을 출력

import sys

input = sys.stdin.readline
s = list(input().rstrip())
t = list(input().rstrip())
# B -> BA -> ABB -> ABBA
# AB -> ABA -> ABAB
# A -> AB -> ABA -> ABAB
while len(s) != len(t):
    # t에서 s로 가려면 A를 제거
    if t[-1] == 'A':
        t.pop()
    # t에서 s로 가려면 B가 제거되고 뒤집어야됨
    elif t[-1] == 'B':
        t.pop()
        t = t[::-1]
    # print(t)

if s == t:
    print(1)
else:
    print(0)
