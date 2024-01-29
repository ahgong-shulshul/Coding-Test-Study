# 24.01.29(월)
# Bronze1
# 문자열
# Solved

n = int(input())
words = []
for i in range(n):
    words.append(input())

str = ""
for i in range(len(words[0])):
    flag = 0
    ch = words[0][i]
    for j in range(len(words)):
        if words[j][i] != ch:
            str += "?"
            flag = 1
            break
    if flag == 0:
        str += ch

print(str)
