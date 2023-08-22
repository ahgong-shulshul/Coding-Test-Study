# 17609 회문

# 회문이면 0 출력, 유사회문이면 1 출력, 그 외 2 출력

import sys

input = sys.stdin.readline
n = int(input())
for _ in range(n):
    string = input().strip()
    length = len(string) // 2
    start = 0
    end = len(string) - 1
    is_possible = False # 회문인지 아닌지를 판별
    while start < end:
        # 회문이라면
        if string[start] == string[end]:
            start += 1
            end -= 1
            is_possible = True
        # 유사회문 또는 회문이 아니라면
        else:
            is_possible = False
            if start <= end-1:
                temp = string[:end] + string[end+1:]
                if temp[:] == temp[::-1]:
                    print(1)
                    break
            if start+1 < end:
                temp = string[:start] + string[start+1:]
                if temp[:] == temp[::-1]:
                    print(1)
                    break
            print(2)
            break
    if is_possible:
        print(0)
                