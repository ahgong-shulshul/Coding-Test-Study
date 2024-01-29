# 17413 단어 뒤집기 2

# <로 시작해서 >로 끝나는 문자열은 안 뒤집고, 그 외의 문자열만 뒤집는 프로그램

import sys

input = sys.stdin.readline
string = list(input().rstrip())
result = ''
while len(string) != 0:
    if string[0] == '<':
        while len(string) != 0 and string[0] != '>':
            s = string.pop(0)
            result += s
        result += string.pop(0)
    else:
        temp = ''
        while len(string) != 0:
            # print(temp)
            if string[0] == '<':
                break
            s = string.pop(0)
            if s == ' ':
                temp += ' '
                if string[0].isalnum():
                    break
            temp = s + temp

        result += temp
print(result)
