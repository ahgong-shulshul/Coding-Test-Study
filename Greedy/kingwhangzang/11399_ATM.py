people = int(input())
list = []
result = 0
time = 0
#입력받기
for num in range(people) :
    num = int(input())
    list.append(num)

list.sort()

#시간 계산
for i in range(people):
    time += list[i]
    result += time

print(result)
    