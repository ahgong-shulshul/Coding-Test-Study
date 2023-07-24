# 18870
# Silver2
# 정렬 알고리즘
# 풀이 날짜: 2023-07-24


n = int(input())
num = [int(m) for m in input().split()]

new = list(set(num))
new.sort()

dic = {}
for i in range(len(new)):
    dic[new[i]] = i

for i in num:
    print(dic[i], end=" ")