# 10814 나이순 정렬

# 나이순 오름차순 정렬 -> 나이가 같다면 가입한 순으로 한 줄에 한 명씩 출력

import sys

input = sys.stdin.readline
n = int(input())
people = []
for _ in range(n):
    age, name = input().split()
    temp = []
    temp.append(int(age))
    temp.append(name)
    people.append(temp)

people.sort(key=lambda x: x[0])  # 나이로만 정렬

for i in range(n):
    age, name = people[i]
    print(age, name)
