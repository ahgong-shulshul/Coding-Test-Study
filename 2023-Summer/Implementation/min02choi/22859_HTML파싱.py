# 22859 HTML 파싱
# Gold3
# Implementation 알고리즘
# 풀이 날짜: 2023-07-13


html = input()
html = list(html)

sub_tag_open = 0
idx = 0

# <p>안의 불필요한 태그 삭제
while ("".join(html[idx:idx + 8]) != "</main>"):
    if ("".join(html[idx:idx + 3]) == "<p>"):
        idx += 3
        while ("".join(html[idx:idx + 4]) != "</p>"):
            if (html[idx] == "<"):
                sub_tag_open = 1
            elif (html[idx] == ">"):
                sub_tag_open = 0
                html[idx] = ""

            if (sub_tag_open == 1):
                html[idx] = ""
            idx += 1
    idx += 1

# 두개 이상의 공백 제거
sentence = "".join(html)
# html = sentence.replace("  ", " ")
html = " ".join(sentence.split())

idx = 0
title = ""
sent = ""
# 문장 좌우의 공백 제거
while ("".join(html[idx:idx + 8]) != "</main>"):
    if ("".join(html[idx:idx + 4]) == "<div"):
        idx += 12
        while (html[idx] != '"'):
            title += html[idx]
            idx += 1
        print("title : " + title)
        title = ""
    
    if ("".join(html[idx:idx + 3]) == "<p>"):
        idx += 3
        while ("".join(html[idx:idx + 4]) != "</p>"):
            sent += html[idx]
            idx += 1
        sen = sent.strip()
        print(sen)
        sent = ""
    idx += 1
