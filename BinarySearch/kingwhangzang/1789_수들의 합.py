num = int(input())
sum = 0
i = 0

while True :
    i += 1
    sum = sum + i
    if sum > num:
        print(i-1)
        break
