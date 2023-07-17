people = int(input())
list = []
result = 0

#입력받기
for num in range(people) :
    num = int(input())
    list.append(num)

list.sort(reverse = True)

#팁 계산
for i in range(people) :
    if list[i] - i < 0:
        continue
    result += (list[i] - i)

print(result)