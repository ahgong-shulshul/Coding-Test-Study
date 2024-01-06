coins = [5, 2]
money = int(input())
count = 0

count = money // 5
money = money % 5

if money % 2 == 1:
    count -= 1
    money += 5
    count = count + money // 2

elif money % 2 == 0:
    count = count + money // 2

print(count)