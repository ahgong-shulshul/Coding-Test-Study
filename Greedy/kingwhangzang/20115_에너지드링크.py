n = int(input())
drinks = [int(m) for m in input().split()]
drinks.sort(reverse = True)

total = drinks[0]
for i in range(1,n): #첫 번째 드링크는 이미 더했으니 다음 드링크부터
    total += (drinks[i]/2) #절반씩 더해줌
    
print(total)