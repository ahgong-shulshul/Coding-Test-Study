# 17413 단어 뒤집기2
# Silver3
# String
# 풀이 날짜: 2023-08-26


# 열림 태그가 나온 경우에는 pass
# 단어를 뒤집는 함수

def word_backward(text):
    temp = ""
    for i in range(len(text)):
        temp = text[i] + temp
    return temp


s = input()

sent = ""
word = ""
open = 0
for i in range(len(s)):
    if s[i] == "<":
        sent += word_backward(word)
        word = ""
        open = 1
    elif s[i] == ">":
        open = 0
        sent += s[i]

    if open == 1:
        sent += s[i]
                
    else:
        if s[i] == " " or s[i] == "<" or i - 1 == len(s):
            sent += word_backward(word)
            if s[i] == " ":
                sent += " "
            word = ""
        elif s[i] != ">":
            word += s[i]

if word != "":
    sent += word_backward(word)

print(sent)
