# 20291 파일 정리
# Silver3
# String
# 풀이 날짜: 2023-08-25

# 딕셔너리 자료구조 사용

n = int(input())

dic = {}
for i in range(n):
    file = input().split(".")[-1]
    if (file in dic):
        dic[file] += 1
    else:
        dic[file] = 1

dic = dict(sorted(dic.items()))

for key, value in dic.items():
    print(key, value)