# 22859 HTML 파싱
# Gold3
# Implementation 알고리즘
# 풀이 날짜: 2023-07-13


html = input()
first_parse = ""

# <p>안의 태그들 다 삭제
for i in range(len(html)):
    if (html[i] == "<" and html[i + 1] == "p"):
        
